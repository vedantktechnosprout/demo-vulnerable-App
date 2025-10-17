FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt  # No --no-cache-dir: Vulnerable to cache bloat/secrets

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
