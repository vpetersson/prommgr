FROM python:3.5
COPY app /app
RUN pip install -r /app/requirements.txt
WORKDIR /app
RUN python manage.py collectstatic --noinput
ENV PYTHONUNBUFFERED 1
CMD [ "gunicorn", "-b", "0.0.0.0:8000", "--workers", "4", "prommgr.wsgi" ]
