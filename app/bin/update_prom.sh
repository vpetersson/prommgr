#!/bin/bash

while true; do
  python manage.py update_prom_config --delete
  python manage.py update_prom_config
  sleep 300
done
