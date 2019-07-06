FROM ubuntu:latest
COPY ./nginx /etc/nginx
COPY . /wtg
WORKDIR /wtg
RUN apt-get update && apt-get install -y python3 python3-pip nginx
RUN pip3 install -r requirements.txt
RUN ln -s /etc/nginx/sites-available/wtg /etc/nginx/sites-enabled
RUN rm /etc/nginx/sites-enabled/default
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
EXPOSE 80 443
CMD ["sh", "-c", "gunicorn -b unix:/tmp/wtg.sock wsgi:app --daemon"]
