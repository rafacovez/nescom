# syntax=docker/dockerfile:1

# ─── Node builder: Tailwind CSS v4 ───────────────────────────────────────────
FROM node:20-slim AS node-builder
WORKDIR /app
COPY package.json package-lock.json* .npmrc* ./
RUN npm ci
COPY . .
RUN npm run build


# ─── Python builder ──────────────────────────────────────────────────────────
FROM python:3.14-slim AS builder

RUN mkdir /app
WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
COPY --from=node-builder /app/static/ ./static/

RUN SECRET_KEY=*** python manage.py collectstatic --noinput


# ─── Runtime ─────────────────────────────────────────────────────────────────
FROM python:3.14-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq5 \
    && rm -rf /var/lib/apt/lists/*

RUN useradd -m -r appuser && \
    mkdir /app && \
    chown -R appuser /app

COPY --from=builder /usr/local/lib/python3.14/site-packages/ /usr/local/lib/python3.14/site-packages/
COPY --from=builder /usr/local/bin/ /usr/local/bin/

WORKDIR /app

COPY --chown=appuser:appuser . .
COPY --from=builder --chown=appuser:appuser /app/staticfiles ./staticfiles

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN printf '#!/bin/sh\n\
set -e\n\
python manage.py migrate --noinput\n\
exec "$@"\n' > /entrypoint.sh && chmod +x /entrypoint.sh

USER appuser

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=5s --start-period=15s --retries=3 \
    CMD python manage.py check --deploy --fail-level WARNING

ENTRYPOINT ["/entrypoint.sh"]
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "3", \
     "--access-logfile", "-", "--error-logfile", "-", \
     "nescom.wsgi:application"]