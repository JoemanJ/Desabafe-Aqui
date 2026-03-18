FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && \
    apt-get install -y sqlite3

COPY requirements.txt /app/
RUN pip install -r requirements.txt

COPY . .

CMD ["python3", "desabafeAqui/manage.py", "runserver", "0.0.0.0:8000"]