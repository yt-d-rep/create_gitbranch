#!/usr/bin/env bash

cd /python

# run wsgi
uwsgi --socket 0.0.0.0:80 --protocol=http -w wsgi:app

# run nginx
nginx -g "daemon off;"