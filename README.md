# Nescom RD

A modern, high-performance corporate website for **Nescom RD**, built with Python v3, Django v6,
django-cotton v2, Wagtail CMS, HTMX, Tailwind CSS v4, and DaisyUI v5.

## Disclaimer

This repository is public for portfolio and deployment purposes only.

The source code is **not open source** and is **not accepting contributions**. Unless otherwise
stated, all rights are reserved by the author. Please refer to the `LICENSE` file for the terms
governing the use, copying, and distribution of this software.

## Development

To start the development environment, run the following commands in separate terminals:

```bash
python manage.py runserver
```

```bash
npm run watch:css
```

## Deployment

A GitHub Actions workflow builds and publishes a multi-architecture Docker image whenever a new
version tag is pushed to the `main` branch.

Example:

```bash
git tag v1.0.0
git push origin v1.0.0
```
