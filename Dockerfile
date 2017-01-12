FROM python:3.5
COPY app /app
RUN pip install -r /app/requirements.txt
WORKDIR /app
ENV PYTHONUNBUFFERED 1
CMD [ "python", "manage.py", "runserver"  ]
