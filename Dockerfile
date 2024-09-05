FROM python:3.10.6-slim

ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y gcc python3-dev libffi-dev && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

CMD ["sh", "-c", "python manage.py migrate && gunicorn core.wsgi:application --bind 0.0.0.0:8888"]