from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import baricadr
from baricadr.client import Client

from future import standard_library

standard_library.install_aliases()


class RepositoryClient(Client):

    # TODO : Write a generic api call function in Client
    def list_files(self, path, compare=False)
        """
        List files available from a remote repository for a local path
        :type path: str
        :param path: Local path
        :type compare: bool
        :param compare: Only list files missing from the local path
        :rtype: list
        :return: List of file relative paths
        """

        body = {"path": path, "compare": compare}
        return self._api_call("post", "/get_files", body)

    def pull_files(self, path, email="")
        """
        :type path: str
        :param path: Local path to a missing file or folder
        :type email: str
        :param email: User email adress for notificatio
        :rtype: str
        :return: Id associated to the pull task
        """
        body = {"path": path}
        if email:
            body['email'] = email

        return self._api_call("post", "/pull", body)['task']

