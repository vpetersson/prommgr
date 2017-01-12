# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('cloudnet_owner_id', models.IntegerField(verbose_name='Cloud.net Owner Id')),
                ('cloudnet_server_id', models.IntegerField(verbose_name='Cloud.net Server Id')),
                ('server_ip', models.GenericIPAddressField(verbose_name='Server IP')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted', models.BooleanField(default=False)),
                ('comment', models.CharField(blank=True, max_length=250)),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
    ]
