#!/usr/bin/env bash
set -euo pipefail

repo_name="haifengxu.com"
project_name="haifengxu-com"

if ! command -v gh >/dev/null 2>&1; then
  echo "gh is required" >&2
  exit 1
fi

if ! command -v wrangler >/dev/null 2>&1; then
  echo "wrangler is required" >&2
  exit 1
fi

if ! gh auth status >/dev/null 2>&1; then
  echo "GitHub auth missing. Run: gh auth login" >&2
  exit 1
fi

if ! wrangler whoami >/dev/null 2>&1; then
  echo "Cloudflare auth missing. Run: wrangler login" >&2
  exit 1
fi

if ! gh repo view "haifengxu/${repo_name}" >/dev/null 2>&1; then
  gh repo create "haifengxu/${repo_name}" --public --source=. --remote=origin --push
else
  git remote remove origin >/dev/null 2>&1 || true
  git remote add origin "git@github.com:haifengxu/${repo_name}.git"
fi

if ! wrangler pages project list | rg -q "^${project_name}\b"; then
  wrangler pages project create "${project_name}" --production-branch main
fi

cat <<MSG
Remote bootstrap complete.

Next in Cloudflare Pages:
- Connect the GitHub repo haifengxu/${repo_name}
- Set Root directory to /
- Build command: hugo --gc --minify -b \$CF_PAGES_URL
- Output directory: public
- Environment variables:
  - HUGO_VERSION=0.157.0
  - HUGO_ENV=production
- Add custom domain: haifengxu.com
- Redirect www.haifengxu.com to haifengxu.com
MSG
