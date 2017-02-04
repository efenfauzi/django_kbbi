heroku run python manage.py migrate
heroku run python manage.py makemigrations kbbi
heroku run python manage.py migrate kbbi --fake
web: gunicorn django_kbbi.wsgi:application -w 4 --log-file -
