# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='server',
            name='server_port',
            field=models.IntegerField(default=9100, verbose_name='Server Port'),
        ),
    ]
