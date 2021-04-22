FROM python:3.8

RUN apt-get update && apt-get -y upgrade

COPY requirements.txt .

RUN pip install -r requirements.txt

WORKDIR /usr/src
                      
