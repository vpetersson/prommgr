# prommgr
A Prometheus management framework.


## Local development setup (non-docker)

```
$ virtualenv venv
$ source venv/bin/activate
$ cd app
$ python manage.py syncdb
[...]
$ python manage.py migrate
$ python manage.py runserver
```

## Local development (docker)

```
$ docker-compose up
$ docker-compose exec prommgr python manage.py syncdb
```

Depending on if the database is ready by the time Django starts, you may also have to run:
```
$ docker-compose restart prommgr
```

To write and delete Prometheus configs, use:
```
$ docker-compose exec prommgr python manage.py write_config --delete
$ docker-compose exec prommgr python manage.py write_config
```
