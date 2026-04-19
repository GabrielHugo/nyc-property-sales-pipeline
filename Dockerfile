FROM python:3.12-slim

WORKDIR /app

RUN pip install --no-cache-dir pandas numpy sqlalchemy jupyter mysql-connector-python

COPY . /app/

CMD ["python", "scripts/main.py"]