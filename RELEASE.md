# Release process (Thomas Webbyrå)

## Before you release
- Pull latest:
  - `git pull`
- Run locally:
  - `python manage.py runserver`
- Smoke test locally:
  - `/`
  - `/admin/`
  - `/portal/`
  - `/crm/quote/`
  - `/sitemap.xml`
  - `/robots.txt`

## Version bump
- Update `core/__init__.py` `__version__`
- Update `CHANGELOG.md`

## Release
- Commit:
  - `git add .`
  - `git commit -m "release: 0.2.0"`
- Tag:
  - `git tag -a v0.2.0 -m "Release 0.2.0"`
- Push:
  - `git push`
  - `git push --tags`

## After deploy (Heroku)
- Check logs:
  - `heroku logs --tail --app <APPNAME>`
- Confirm release phase ran:
  - migrations + collectstatic
- Smoke test live:
  - `/`
  - `/admin/`
  - `/sitemap.xml`
  - `/robots.txt`