import os
from django.core.management.base import BaseCommand
from restapi.models import Server
from lib import prom_helper

PROM_CONFIG_PATH = os.getenv('PROM_CONFIG_PATH', '/prom/targets')


def delete_prom_config(server):
    config_file = os.path.join(
        PROM_CONFIG_PATH,
        '{}.yml'.format(server.id)
    )

    if os.path.exists(config_file):
        os.remove(config_file)


def write_prom_config(server):
    config_file = os.path.join(
        PROM_CONFIG_PATH,
        '{}.yml'.format(server.id)
    )
    get_config = prom_helper.generate_prom_server_config(server)
    with open(config_file, 'w') as f:
        f.write(get_config)


class Command(BaseCommand):
    help = 'Manage server configurations.'

    def add_arguments(self, parser):
        parser.add_argument(
            '--delete',
            action='store_true',
            dest='delete',
            default=False,
            help='Delete configs for deleted servers.'
        )

    def handle(self, *args, **options):
        if options['delete']:
            for server in Server.objects.filter(deleted=True):
                delete_prom_config(server)
        else:
            for server in Server.objects.filter(deleted=False):
                write_prom_config(server)
