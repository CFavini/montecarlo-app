FROM python:3.11.9-slim

ENV PYTHONUNBUFFERED=1
WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt gunicorn

COPY . .

CMD ["gunicorn", "-b", "0.0.0.0:8080", "backend.app:create_app()"]