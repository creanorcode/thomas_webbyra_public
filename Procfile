release: python manage.py migrate --noinput && python manage.py collectstatic --noinput
web: gunicorn core.wsgi:application --log-file -