FROM python:3.12

WORKDIR /home/app

COPY . /home/app/

ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip
RUN pip install -r requirements.txt