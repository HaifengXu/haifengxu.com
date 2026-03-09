#!/usr/bin/env python3

from __future__ import annotations

import argparse
import re
import shutil
import sys
from datetime import datetime
from pathlib import Path


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-") or "post"


def parse_bool(raw: str) -> bool:
    lowered = raw.strip().lower()
    if lowered in {"true", "1", "yes", "y"}:
        return True
    if lowered in {"false", "0", "no", "n"}:
        return False
    raise argparse.ArgumentTypeError(f"invalid boolean value: {raw}")


def infer_title_and_body(text: str, fallback_title: str) -> tuple[str, str]:
    lines = text.splitlines()
    if lines and lines[0].startswith("# "):
        title = lines[0][2:].strip() or fallback_title
        body = "\n".join(lines[1:]).lstrip("\n")
        return title, body
    return fallback_title, text.lstrip()


def sentence_case(value: str) -> str:
    if not value:
        return value
    return value[0].lower() + value[1:]


def clean_heading(value: str) -> str:
    value = re.sub(r"`([^`]+)`", r"\1", value)
    value = re.sub(r"\*([^*]+)\*", r"\1", value)
    value = value.replace('"', "")
    return re.sub(r"\s+", " ", value).strip(" .:-")


def infer_description(title: str, body: str) -> str:
    headings: list[str] = []
    for line in body.splitlines():
        if line.startswith("## "):
            heading = clean_heading(line[3:].strip())
            if heading:
                headings.append(heading)

    if title and headings:
        heading = sentence_case(headings[0])
        if re.match(r"^(why|how|when|what)\b", heading):
            description = heading[0].upper() + heading[1:] + "."
        else:
            description = f"When {heading}."
        if len(description) <= 160:
            return description

    for block in re.split(r"\n\s*\n", body):
        stripped = block.strip()
        if not stripped:
            continue
        if stripped.startswith("#"):
            continue
        if stripped.startswith("!["):
            continue
        single_line = re.sub(r"\s+", " ", stripped)
        return single_line[:157] + "..." if len(single_line) > 160 else single_line
    return ""


def toml_escape(value: str) -> str:
    return value.replace("\\", "\\\\").replace('"', '\\"')


def asset_name(filename: str) -> str:
    path = Path(filename)
    stem = slugify(path.stem)
    suffix = path.suffix.lower()
    return f"{stem}{suffix}"


def rewrite_obsidian_embeds(body: str, source_dir: Path, static_dir: Path, slug: str) -> str:
    target_dir = static_dir / "posts" / slug
    target_dir.mkdir(parents=True, exist_ok=True)

    def replace(match: re.Match[str]) -> str:
        original = match.group(1).strip()
        source_asset = source_dir / original
        if not source_asset.is_file():
            return f"*Missing embedded asset: {original}*"
        copied_name = asset_name(original)
        shutil.copy2(source_asset, target_dir / copied_name)
        alt = Path(original).stem.replace("-", " ").replace("_", " ").strip()
        return f"![{alt}](/posts/{slug}/{copied_name})"

    return re.sub(r"!\[\[([^\]]+)\]\]", replace, body)


def rewrite_markdown_images(body: str, source_dir: Path, static_dir: Path, slug: str) -> str:
    target_dir = static_dir / "posts" / slug
    target_dir.mkdir(parents=True, exist_ok=True)

    def replace(match: re.Match[str]) -> str:
        alt = match.group(1)
        raw_path = match.group(2).strip()
        if raw_path.startswith(("http://", "https://", "/")):
            return match.group(0)
        source_asset = (source_dir / raw_path).resolve()
        try:
            source_asset.relative_to(source_dir.resolve())
        except ValueError:
            return match.group(0)
        if not source_asset.is_file():
            return match.group(0)
        copied_name = asset_name(source_asset.name)
        shutil.copy2(source_asset, target_dir / copied_name)
        return f"![{alt}](/posts/{slug}/{copied_name})"

    return re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", replace, body)


def read_existing_front_matter_value(path: Path, key: str) -> str | None:
    if not path.is_file():
        return None
    text = path.read_text(encoding="utf-8")
    if not text.startswith("+++\n"):
        return None
    parts = text.split("+++\n", 2)
    if len(parts) < 3:
        return None
    front_matter = parts[1]
    match = re.search(rf'^{re.escape(key)}\s*=\s*"((?:[^"\\]|\\.)*)"$', front_matter, re.MULTILINE)
    if not match:
        return None
    value = match.group(1)
    return value.replace('\\"', '"').replace("\\\\", "\\")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Convert a markdown file into a Hugo post in content/posts/."
    )
    parser.add_argument("source", help="Path to the source markdown file")
    parser.add_argument("--repo", required=True, help="Path to the Hugo site repo root")
    parser.add_argument("--slug", help="Output slug")
    parser.add_argument("--title", help="Post title")
    parser.add_argument("--date", help="ISO 8601 date for front matter")
    parser.add_argument("--description", help="Post description")
    parser.add_argument("--tags", help="Comma-separated tag list")
    parser.add_argument("--draft", type=parse_bool, default=False, help="Draft status")
    parser.add_argument("--featured", type=parse_bool, default=False, help="Featured status")
    parser.add_argument(
        "--force", action="store_true", help="Overwrite an existing output file if present"
    )
    args = parser.parse_args()

    source_path = Path(args.source).expanduser().resolve()
    repo_path = Path(args.repo).expanduser().resolve()
    if not source_path.is_file():
        print(f"Source file not found: {source_path}", file=sys.stderr)
        return 1
    posts_dir = repo_path / "content" / "posts"
    static_dir = repo_path / "static"
    if not posts_dir.is_dir():
        print(f"Posts directory not found: {posts_dir}", file=sys.stderr)
        return 1
    if not static_dir.is_dir():
        print(f"Static directory not found: {static_dir}", file=sys.stderr)
        return 1

    raw_text = source_path.read_text(encoding="utf-8")
    fallback_title = args.title or source_path.stem.replace("-", " ").replace("_", " ").strip().title()
    inferred_title, body = infer_title_and_body(raw_text, fallback_title)
    title = args.title or inferred_title
    slug = args.slug or slugify(title or source_path.stem)
    body = rewrite_obsidian_embeds(body, source_path.parent, static_dir, slug)
    body = rewrite_markdown_images(body, source_path.parent, static_dir, slug)
    date = args.date or datetime.now().astimezone().isoformat(timespec="seconds")

    output_path = posts_dir / f"{slug}.md"
    if output_path.exists() and not args.force:
        print(f"Refusing to overwrite existing file: {output_path}", file=sys.stderr)
        return 1

    existing_description = None
    if output_path.exists() and args.force and args.description is None:
        existing_description = read_existing_front_matter_value(output_path, "description")

    description = args.description or existing_description or infer_description(title, body)
    tags = [tag.strip() for tag in (args.tags or "").split(",") if tag.strip()]
    toc = "## " in body

    tags_literal = ", ".join(f'"{toml_escape(tag)}"' for tag in tags)

    front_matter = [
        "+++",
        f'title = "{toml_escape(title)}"',
        f"date = {date}",
        f"draft = {'true' if args.draft else 'false'}",
        f'description = "{toml_escape(description)}"',
        f"tags = [{tags_literal}]",
        "categories = []",
        f"toc = {'true' if toc else 'false'}",
        "readingTime = true",
        f"featured = {'true' if args.featured else 'false'}",
        "+++",
        "",
    ]
    content = "\n".join(front_matter) + body.rstrip() + "\n"
    output_path.write_text(content, encoding="utf-8")
    print(output_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
