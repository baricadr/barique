from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from baricadr.client import Client

from future import standard_library

standard_library.install_aliases()


class FileClient(Client):
    """
    Manipulate files managed by Baricadr
    """

    def list(self, path, missing=False, max_depth=1):
        """
        List files available from a remote repository for a local path

        :type path: str
        :param path: Local path

        :type missing: bool
        :param missing: Only list files missing from the local path

        :type max_depth: int
        :param max_depth: Restrict to a max depth. Set to 0 for all files.

        :rtype: list
        :return: List of file relative paths
        """

        body = {"path": path, "missing": missing, "max_depth": max_depth}
        return self._api_call("post", "list", body)

    def pull(self, path, email=""):
        """
        Launch a pull task

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

        return self._api_call("post", "pull_files", body)['task']
