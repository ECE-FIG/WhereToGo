FROM alpine
COPY ./nginx /etc/nginx
COPY . /wtg
WORKDIR /wtg
RUN apk update && apk add python3 nginx
RUN pip3 install -r requirements.txt
RUN mkdir -p /etc/nginx/sites-enabled
RUN ln -s /etc/nginx/sites-available/wtg /etc/nginx/sites-enabled/
RUN mkdir -p /run/nginx
RUN mkdir -p /var/log/gunicorn
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
EXPOSE 80 443
CMD ["sh", "-c", "nginx && gunicorn -b unix:/tmp/wtg.sock \
    --access-logfile /var/log/gunicorn/access.log \
    --error-logfile /var/log/gunicorn/error.log \
    wsgi:app"]
