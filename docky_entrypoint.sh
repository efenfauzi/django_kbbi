#!/bin/bash
python manage.py migrate --fake
python manage.py makemigrations kbbi
python manage.py migrate kbbi --fake
python manage.py collectstatic --noinput

echo Starting Gunicorn.
exec gunicorn django_kbbi.wsgi:application \
    --name django_kbbi \
    --bind 0.0.0.0:6565 \
    --workers 4 \
    "$@"
