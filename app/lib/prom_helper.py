

def generate_prom_server_config(server):
    """
    Generates a Prometheus configuration file.
    """

    # Sanity check input
    try:
        server.server_ip
        server.server_port
    except:
        print('Unable to load keys.')
        return False

    return """
- targets: [ '{}:{}' ]
""".format(
        server.server_ip,
        server.server_port,
    )
