web: python manage.py migrate
web: python manage.py makemigrations kbbi
web: python manage.py migrate kbbi --fake
web: gunicorn django_kbbi.wsgi:application --log-file -
