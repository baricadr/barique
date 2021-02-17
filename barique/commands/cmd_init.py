# coding: utf-8
import os

import click

from baricadr import BaricadrInstance
from barique.cli import pass_context
from barique import config
from barique.io import warn, info

CONFIG_TEMPLATE = """## Baricadr's barique: Global Configuration File.
# Each stanza should contain a single baricadr server to control.
#
# You can set the key __default to the name of a default instance
__default: local
local:
    host: "%(host)s"
    port: "%(port)s"
"""

CONFIG_TEMPLATE_AUTH = """## Baricadr's barique: Global Configuration File.
# Each stanza should contain a single baricadr server to control.
#
# You can set the key __default to the name of a default instance
__default: local
local:
    host: "%(host)s"
    port: "%(port)s"
    login: "%(login)s"
    password: "%(password)s"
"""

SUCCESS_MESSAGE = (
    "Ready to go! Type `barique` to get a list of commands you can execute."
)


@click.command("config_init")
@pass_context
def cli(ctx, url=None, api_key=None, admin=False, **kwds):
    """Help initialize global configuration (in home directory)
    """

    click.echo("""Welcome to Barique""")
    if os.path.exists(config.global_config_path()):
        info("Your barique configuration already exists. Please edit it instead: %s" % config.global_config_path())
        return 0

    while True:
        # Check environment
        host = click.prompt("Baricadr server host")
        port = click.prompt("Baricadr server port")
        login = None
        password = None
        if click.confirm("""Is your Baricadr instance running behind an authentication proxy?"""):
            login = click.prompt("Baricadr username")
            password = click.prompt("Baricadr password", hide_input=True)

        info("Testing connection...")
        try:
            BaricadrInstance(host=host, port=port, login=login, password=password)
            # We do a connection test during startup.
            info("Ok! Everything looks good.")
            break
        except Exception as e:
            warn("Error, we could not access the configuration data for your instance: %s", e)
            should_break = click.prompt("Continue despite inability to contact this instance? [y/n]")
            if should_break in ('Y', 'y'):
                break

    config_path = config.global_config_path()
    if os.path.exists(config_path):
        warn("File %s already exists, refusing to overwrite." % config_path)
        return -1

    with open(config_path, "w") as f:
        if login and password:
            f.write(CONFIG_TEMPLATE_AUTH % {
                'host': host,
                'port': port,
                'login': login,
                'password': password,
            })
        else:
            f.write(CONFIG_TEMPLATE % {
                'host': host,
                'port': port,
            })
        info(SUCCESS_MESSAGE)

    # We don't want other users to look into this file
    os.chmod(config_path, 0o600)
