from __future__ import absolute_import

import os

from baricadr import BaricadrInstance

import yaml

DEFAULT_CONFIG = {
}

_config_path = os.environ.get(
    "BARIQUE_GLOBAL_CONFIG_PATH",
    "~/.barique.yml"
)
_config_path = os.path.expanduser(_config_path)
DEFAULT_CONFIG['config_path'] = _config_path


def global_config_path():
    return DEFAULT_CONFIG['config_path']


def set_global_config_path(config_path):
    DEFAULT_CONFIG['config_path'] = config_path


def read_global_config():
    config_path = global_config_path()
    if not os.path.exists(config_path):
        return DEFAULT_CONFIG

    with open(config_path) as f:
        return yaml.safe_load(f)


def _get_instance(instance_name=None):
    # I don't like reading the config twice.
    conf = read_global_config()

    if not os.path.exists(global_config_path()):
        # Probably creating the file for the first time.
        return None

    if instance_name is None or instance_name == '__default':
        try:
            instance_name = conf['__default']
        except KeyError:
            raise Exception("Unknown Baricadr instance and no __default provided")

    if instance_name not in conf:
        raise Exception("Unknown Baricadr instance; check spelling or add to %s" % DEFAULT_CONFIG)

    return conf[instance_name]


def get_instance(instance_name=None):
    conf = _get_instance(instance_name=instance_name)

    login = None
    password = None
    if 'login' in conf and 'password' in conf:
        login = conf['login']
        password = conf['password']

    return BaricadrInstance(host=conf['host'],
                            port=conf['port'],
                            login=login,
                            password=password,
                            )
