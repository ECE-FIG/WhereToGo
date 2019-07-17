FROM alpine
COPY . /srv/idkwheretogo/www
WORKDIR /srv/idkwheretogo/www
RUN apk update && apk add python3
RUN pip3 install -r requirements.txt
RUN mkdir -p /var/log/gunicorn
EXPOSE 5000
CMD ["sh", "-c", "gunicorn -b 0.0.0.0:5000 \
    --access-logfile /var/log/gunicorn/access.log \
    --error-logfile /var/log/gunicorn/error.log \
    wsgi:app"]
