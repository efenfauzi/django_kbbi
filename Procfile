python manage.py migrate
python manage.py makemigrations kbbi
python manage.py migrate kbbi --fake
web: gunicorn django_kbbi.wsgi:application --log-file -
