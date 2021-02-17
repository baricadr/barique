from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from baricadr.exceptions import BaricadrConnectionError
from baricadr.file import FileClient
from baricadr.task import TaskClient

from future import standard_library

import requests

standard_library.install_aliases()


class BaricadrInstance(object):

    def __init__(self, host="localhost", port="9100", login=None, password=None, **kwargs):
        self.host = host
        self.port = str(port)

        self.login = login
        self.password = password

        self.endpoints = self._get_endpoints()

        # Initialize Clients
        args = (self.host, self.port, self.login, self.password, self.endpoints)
        self.file = FileClient(*args)
        self.task = TaskClient(*args)

    def __str__(self):
        return '<BarricadrInstance at {}:{}>'.format(self.host, self.port)

    def _get_endpoints(self):

        auth = None
        if self.login and self.password:
            auth = (self.login, self.password)

        try:
            r = requests.get("http://{}:{}/endpoints".format(self.host, self.port), auth=auth)
            if not r.status_code == 200:
                raise requests.exceptions.RequestException
            return r.json()
        except requests.exceptions.RequestException:
            raise BaricadrConnectionError("Cannot connect to {}:{}. Please check the connection.".format(self.host, self.port))
