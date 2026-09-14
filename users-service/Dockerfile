# Pinned to the exact Python patch release so every student builds an identical image.
# Python 3.13 is supported until 2029-10-31; 3.10 reaches end-of-life on 2026-10-31.
FROM python:3.13.15-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
