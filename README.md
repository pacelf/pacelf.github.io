# PacELF Digital Library

The production website is https://pacelf.github.io/.
This repository contains Jekyll source, the public catalogue, and public PDFs.
Catalogue preparation is maintained separately in `pacelf/data-prep`.

## Local preview

Use the Ruby version in `.ruby-version` and the committed `Gemfile.lock`:

```bash
bundle install
bundle exec jekyll serve
```

Open http://127.0.0.1:4000/. For a production build:

```bash
JEKYLL_ENV=production bundle exec jekyll build
```

Do not commit `_site/`, caches, or installed gems. Before the first production
release, pin `remote_theme` in `_config.yml` to the approved RWT release tag.
Update that reference deliberately when adopting a later theme release.

## Catalogue updates

In the separate data preparation repository, the production download template is
`website.open.url: /library/documents/{filename}` in `scripts/library-config.yml`.
Generate and review the data there, then copy `jcudlc-data.json`,
`jcudlc-config.json`, and the required public documents into this repository's
`library/` directory. The source workbook and private documents do not belong
in this public repository.

The phase9-draft repository remains a separate preview site. Its downloads need
the `/phase9-draft` prefix; use that configuration when preparing preview data.

## Build and publication

The `.github/workflows/github-pages.yml` workflow:

- Builds and validates pushes and pull requests targeting `main` without deploying.
- Deploys the tagged source when a stable GitHub release is published.
- Ignores draft releases and prereleases for production deployment.
- Can be run manually with an existing Jekyll release tag for redeployment or rollback.

Configure Pages to use GitHub Actions. The `github-pages` deployment environment
must allow release tags; a main-only rule will block release deployments.
Publishing a release starts deployment; check the Actions result and the live
site before considering publication complete. Editing/deleting a release or
reverting main alone does not change the deployed site.

To roll back a Jekyll release, open Actions → Build and publish PacELF → Run
workflow, choose `main` as the workflow branch, and enter the older release tag
in `release_tag`. Avoid overlapping release and rollback operations. A later
stable release deployment replaces the rollback.

## Compatibility with the old site

- `sw.js` retires the previous Quasar offline cache and reloads affected tabs.
  Keep this file at the original URL for returning visitors.
- `_plugins/legacy_navigation.rb` adds the legacy navigation script to the home
  page and custom 404 page, without copying the theme layouts.
- Old hash bookmarks for library/contact/background map to the replacement
  pages. Background content is now on the home page.
- Old `/documents/<filename>` URLs pass through the custom 404 page to
  `/library/documents/<filename>`. These are browser-side redirects, not HTTP
  redirects; automated download clients may still receive 404 and must use the
  new URL. All 223 previously published PDF basenames exist in the new collection.

## Initial phase9 migration

Migration source: `pacelf/phase9-draft` commit
`1ddfb90c5adfd0e780d0c87bce4cb98f9389e65a`.

Previous production source (`master`):
`ad3e99b850e27c14e1c7b1ec13432c5eabac9231`.

Previous built production (`gh-pages`):
`af04f5e1d399f4e307f1ddcbfa3ffe89e7bfec2e`.

Keep the old `gh-pages` branch during the migration. The Jekyll workflow cannot
build the old Quasar source releases. To restore the old site, change Pages back
to Deploy from a branch → `gh-pages` → `/ (root)` and verify the deployment.

This old-site rollback does not restore the former offline app behaviour:
returning users' old service worker may have been retired by the new site.

See `PUBLISHING.md` for the initial GitHub setup and publication checklist.
