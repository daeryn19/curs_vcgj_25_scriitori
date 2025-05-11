# Imagine de bază cu Python 3.12
FROM python:3.12-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir flask

EXPOSE 5000

CMD ["python", "app.py"]

