FROM python:3.7.3-slim-stretch

RUN apt-get update \
 # install required packages
 && apt-get install -y \
    build-essential \ 
    git \
    nginx \
    python3-dev \
    wget \
 # set timezone
 && ln -sf  /usr/share/zoneinfo/Asia/Tokyo /etc/localtime \
 && dpkg-reconfigure -f noninteractive tzdata \
 # install python modules
 && pip install flask \ 
    uwsgi \
 && mkdir /python \
 # forward request and error logs to docker log collector
 && ln -sf /dev/stdout /var/log/nginx/access.log \
 && ln -sf /dev/stderr /var/log/nginx/error.log

COPY ./conf/default.conf /etc/nginx/conf.d/default.conf
COPY ./app/* /python/
COPY ./entrypoint.sh /

EXPOSE 80

# run
ENTRYPOINT [ "/entrypoint.sh" ]