# syntax=docker/dockerfile:1

# ─── 1. Node builder: Tailwind CSS ───────────────────────────────────────────
FROM node:20-slim AS node-builder
WORKDIR /app
COPY package.json package-lock.json* .npmrc* ./
RUN npm ci
COPY . .
RUN npm run build


# ─── 2. Python builder ──────────────────────────────────────────────────────────
FROM python:3.14-slim AS builder

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    libjpeg-dev \
    zlib1g-dev \
    libwebp-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
# Bring in built CSS/JS before collecting static
COPY --from=node-builder /app/static/ ./static/

RUN SECRET_KEY=build-time-secret-key python manage.py collectstatic --noinput


# ─── 3. Runtime ─────────────────────────────────────────────────────────────────
FROM python:3.14-slim AS runner

# CHANGE THIS to your Django project folder name for new projects
ENV WSGI_APP="nescom.wsgi:application"

# Install runtime dependencies for Postgres & Wagtail image processing
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq5 \
    libjpeg62-turbo \
    zlib1g \
    libwebp7 \
    libopenjp2-7 \
    && rm -rf /var/lib/apt/lists/*

RUN useradd -m -r appuser && \
    mkdir -p /app/media /app/staticfiles && \
    chown -R appuser:appuser /app

WORKDIR /app

# Copy python dependencies
COPY --from=builder /usr/local/lib/python3.14/site-packages/ /usr/local/lib/python3.14/site-packages/
COPY --from=builder /usr/local/bin/ /usr/local/bin/

# Copy application source & built assets
COPY --chown=appuser:appuser . .
COPY --from=node-builder --chown=appuser:appuser /app/static/ ./static/
COPY --from=builder --chown=appuser:appuser /app/staticfiles/ ./staticfiles/

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN printf '#!/bin/sh\n\
set -e\n\
python manage.py migrate --noinput\n\
exec "$@"\n' > /entrypoint.sh && chmod +x /entrypoint.sh

USER appuser

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=5s --start-period=15s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/').read()" || exit 1

ENTRYPOINT ["/entrypoint.sh"]
# Using the WSGI_APP environment variable dynamically
CMD ["sh", "-c", "gunicorn --bind 0.0.0.0:8000 --workers 3 --access-logfile - --error-logfile - ${WSGI_APP}"]