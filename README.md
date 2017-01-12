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
$ docker-compose exec prommgr python manage.py update_prom_config --delete
$ docker-compose exec prommgr python manage.py update_prom_config
```

## API Documentation

For API documentation, spin up the server locally and visit `/docs`.

## Alerts

The system is configured for these alerts (configured in `prom/alerts.rules`)::

 * System is up/down.
 * High CPU load average.
 * High memory usage.
 * Disk is expected to fill up in the next four hours (for root partition).

When an alert is fired, the webhook content will look like this:

```
{'alerts': [{'annotations': {'summary': 'Instance 1.2.3.4:9100 is down'},
             'endsAt': '0001-01-01T00:00:00Z',
             'generatorURL': 'http://0c680b8917a9:9090/graph?g0.expr=up+%3D%3D+0\\u0026g0.tab=0',
             'labels': {'alertname': 'service_down',
                        'cloudnet_owner_id': '11',
                        'cloudnet_server_id': '4386',
                        'instance': '1.2.3.4:9100',
                        'job': 'node'},
             'startsAt': '2017-01-12T14:44:37.805Z',
             'status': 'firing'},
            {'annotations': {'summary': 'Instance 1.2.3.4:9100 is down'},
             'endsAt': '0001-01-01T00:00:00Z',
             'generatorURL': 'http://0c680b8917a9:9090/graph?g0.expr=up+%3D%3D+0\\u0026g0.tab=0',
             'labels': {'alertname': 'service_down',
                        'cloudnet_owner_id': '11',
                        'cloudnet_server_id': '4385',
                        'instance': '1.2.3.4:9100',
                        'job': 'node'},
             'startsAt': '2017-01-12T14:44:37.805Z',
             'status': 'firing'}],
 'commonAnnotations': {},
 'commonLabels': {'alertname': 'service_down',
                  'cloudnet_owner_id': '11',
                  'job': 'node'},
 'externalURL': 'http://56272fa974e2:9093',
 'groupKey': 11840296893788715932L,
 'groupLabels': {'alertname': 'service_down'},
 'receiver': 'webhook',
 'status': 'firing',
 'version': '3'}
```
