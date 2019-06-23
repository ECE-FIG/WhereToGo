FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python3 python3-pip
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
ENV FLASK_APP wtg_frontend.py
ENV FLASK_ENV development
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
CMD flask run --host=0.0.0.0
