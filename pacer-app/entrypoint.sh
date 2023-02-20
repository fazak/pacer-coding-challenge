#!/bin/sh

python3 manage.py collectstatic --no-input

gunicorn pacer.wsgi:application --bind 0.0.0.0:8000
