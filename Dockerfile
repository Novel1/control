FROM python:3.11-slim-buster

WORKDIR /app
COPY requirements.txt /app/

RUN pip3 install --upgrade pip && pip3 install -r requirements.txt

COPY . .