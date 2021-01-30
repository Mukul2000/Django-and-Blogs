web: gunicorn django_blog.wsgi --log-file - --log-level debug
python manage.py collectstatic --noinput
manage.py migrate