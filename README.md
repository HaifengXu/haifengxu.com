# haifengxu.com

A Hugo-powered personal site for weekly writing on tech, reflection, and leadership.

## Local workflow

1. Install Hugo extended.
2. Start a draft-aware dev server:
   ```bash
   make dev
   ```
3. Create a new post:
   ```bash
   make new slug=my-new-post
   ```
4. Produce a production build:
   ```bash
   make build
   ```

## Standalone repo

This directory is initialized as its own Git repository so it can be pushed independently from the main `openclaw` workspace.

- Local repo root: `haifengxu.com/`
- Default branch: `main`
- Bootstrap remote setup after auth:
  ```bash
  ./scripts/bootstrap-remote.sh
  ```

## Authoring contract

- Store posts in `content/posts/`.
- Use the default front matter fields from `archetypes/posts.md`:
  - `title`
  - `date`
  - `draft`
  - `description`
  - `tags`
  - `categories`
  - `toc`
  - `readingTime`
  - `featured`
- Keep `draft = true` until the post is ready to publish.
- Mark only one post as `featured = true` if you want a single highlighted post on the homepage.

## Cloudflare Pages

Recommended settings:

- Framework preset: `Hugo`
- Build command: `hugo --gc --minify -b $CF_PAGES_URL`
- Build output directory: `public`
- Root directory: `/`
- Production branch: your default branch

Set these environment variables in Cloudflare Pages:

- `HUGO_VERSION=0.157.0`
- `HUGO_ENV=production`

After the first successful deploy:

1. Attach the custom domain `haifengxu.com`.
2. Add `www.haifengxu.com` and configure it to redirect to the apex domain.
3. Enable Cloudflare Web Analytics if you want lightweight analytics without adding third-party scripts.

## GitHub Actions

Two workflows are included:

- `.github/workflows/hugo-build.yml`: build validation on pushes and pull requests
- `.github/workflows/cloudflare-pages-preview.yml`: optional preview deploys for pull requests when `CLOUDFLARE_API_TOKEN` and `CLOUDFLARE_ACCOUNT_ID` are configured in the GitHub repo secrets

## Notes

- The theme is custom and does not depend on a third-party Hugo theme.
- The site is intentionally scoped to Home, About, Writing, RSS, and post pages.
