from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import os

from baricadr.client import Client

from future import standard_library

from treelib import Tree

standard_library.install_aliases()


class FileClient(Client):
    """
    Manipulate files managed by Baricadr
    """

    def list(self, path, full=False, missing=False, max_depth=1, from_root=False):
        """
        List files available from a remote repository for a local path

        :type path: str
        :param path: Local path

        :type missing: bool
        :param missing: Only list files missing from the local path

        :type full: bool
        :param full: List full information for each file (size (in bytes), mtime, etc..)

        :type max_depth: int
        :param max_depth: Restrict to a max depth. Set to 0 for all files.

        :type from_root: bool
        :param from_root: Return full paths from root of the repo (instead of relative to given path)

        :rtype: list
        :return: List of file relative paths
        """

        body = {"path": path, "missing": missing, "max_depth": max_depth, "from_root": from_root, "full": full}
        return self._api_call("post", "list", body)

    def pull(self, path, email="", dry_run=False):
        """
        Launch a pull task

        :type path: str
        :param path: Local path to a missing file or folder

        :type email: str
        :param email: User email adress for notification

        :type dry_run: bool
        :param dry_run: Do not make any pull, just list changes that would be made

        :rtype: str
        :return: Id associated to the pull task
        """
        body = {"path": path, "dry_run": dry_run}
        if email:
            body['email'] = email

        return self._api_call("post", "pull", body)['task']

    def freeze(self, path, force=False, dry_run=False, email=""):
        """
        Launch a freeze task

        :type path: str
        :param path: Local path to a file or folder to freeze

        :type force: bool
        :param force: Force freezing, even if the freezing delay was not reached

        :type dry_run: bool
        :param dry_run: Do not make any deletion, just list changes that would be made

        :type email: str
        :param email: User email adress for notification

        :rtype: str
        :return: Id associated to the freeze task
        """
        body = {"path": path, "force": force, "dry_run": dry_run}

        if email:
            body['email'] = email

        return self._api_call("post", "freeze", body)['task']

    def tree(self, path, max_depth=0):
        """
        List files available from a remote repository for a local path as a tree

        :type path: str
        :param path: Local path

        :type max_depth: int
        :param max_depth: Restrict to a max depth. Set to 0 for all files.

        :rtype: None
        :return: None
        """

        body = {"path": path, "max_depth": max_depth}

        return self._print_tree(self._api_call("post", "tree", body), path)

    def _print_tree(self, files, asked_path):
        asked_path = asked_path.rstrip("/")
        # Print the paths as a tree
        tree = Tree()
        tree.create_node(asked_path, ".")
        processed_nodes = set()

        for path in files:
            previous = "."
            current_id = ""
            current_path = path["Path"].rstrip("/")
            current_file = os.path.basename(current_path)
            for fragment in current_path.split("/"):
                current_id = current_id + "_" + fragment if current_id else fragment
                # If last fragment
                if fragment == current_file and path['missing']:
                    fragment += " *"
                if current_id not in processed_nodes:
                    tree.create_node(fragment, current_id, previous)
                    processed_nodes.add(current_id)
                previous = current_id

        tree.show()
