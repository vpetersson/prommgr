import os


def add_server():
    pass


def delete_server():
    pass


def process_server_action(
    action=None,
    user_id=None,
    server_id=None,
    server_ip=None,
):
    pass


def generate_config(
    server_ip=None,
    server_id=None,
    user_id=None
):

    return """
- targets: [ '{}:9100' ]
  labels:
    user_id: '{}'
    server_id: {}
""".format(server_ip, user_id, server_id)
