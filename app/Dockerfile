FROM python:3.9-alpine

LABEL MAINTAINER="Ata İnan <inanata15@gmail.com>"

ENV GROUP_ID=1000 \
    USER_ID=1000

WORKDIR /var/www/

ADD ./requirements.txt /var/www/requirements.txt
RUN pip3 install -r requirements.txt
ADD . /var/www/
RUN pip3 install gunicorn

RUN addgroup -g $GROUP_ID www
RUN adduser -D -u $USER_ID -G www www -s /bin/sh

USER www

EXPOSE 5000

CMD [ "gunicorn", "-w", "4", "--bind", "0.0.0.0:5000", "wsgi"]
