FROM python:3.11.9 AS builder

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1
WORKDIR /app

RUN python -m venv .venv
COPY requirements.txt ./
RUN .venv/bin/pip install -r requirements.txt gunicorn

FROM python:3.11.9-slim
WORKDIR /app
COPY --from=builder /app/.venv .venv/
COPY . .

CMD ["/app/.venv/bin/gunicorn", "-b", "0.0.0.0:8080", "backend.app:create_app()"]