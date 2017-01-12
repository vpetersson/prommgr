import os
from django.core.management.base import BaseCommand
from restapi.models import Server
from lib import prom_helper

PROM_CONFIG_PATH = os.getenv('PROM_CONFIG_PATH', '/prom/targets')


def get_config_file_path(server_id):
    return os.path.join(
        PROM_CONFIG_PATH,
        '{}.yml'.format(server_id)
    )


def delete_prom_config(server):
    config_file = get_config_file_path(server.id)

    if os.path.exists(config_file):
        print('Deleting server: {}'.format(server.id))
        os.remove(config_file)


def write_prom_config(server):
    config_file = get_config_file_path(server.id)
    print('Creating server: {}'.format(server.id))

    generate_config = prom_helper.generate_prom_server_config(server)
    with open(config_file, 'w') as f:
        f.write(generate_config)


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
