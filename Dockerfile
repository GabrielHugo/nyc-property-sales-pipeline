FROM python:3.12-slim

WORKDIR /app

RUN pip install --no-cache-dir pandas numpy sqlalchemy mysql-connector-python

COPY . /app/

CMD ["python", "scripts/main.py"]