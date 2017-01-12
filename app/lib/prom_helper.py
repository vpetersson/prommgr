

def generate_prom_server_config(server):
    """
    Generates a Prometheus configuration file.
    """

    # Sanity check input
    try:
        server.server_ip
        server.server_port
        server.cloudnet_owner_id
        server.cloudnet_server_id
    except:
        print('Unable to load keys.')
        return False

    return """
- targets: [ '{}:{}' ]
  labels:
        cloudnet_owner_id: '{}'
        cloudnet_server_id: {}
""".format(
        server.server_ip,
        server.server_port,
        server.cloudnet_owner_id,
        server.cloudnet_server_id
    )
