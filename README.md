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
