from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from baricadr.client import Client

from future import standard_library

standard_library.install_aliases()


class TaskClient(Client):
    """
    Track progress of Baricadr tasks
    """

    def list(self):
        """
        List recent tasks

        :rtype: list
        :return: List of tasks
        """

        return self._api_call("get", "task_list")

    def show(self, task_id):
        """
        Show task with the specified id

        :type task_id: str
        :param task_id: Task id

        :rtype: dict
        :return: Dict
        """

        args = {"task_id": str(task_id)}

        return self._api_call("get", "task_show", args)

    def log(self, task_id):
        """
        Show log from the task with the specified id

        :type task_id: str
        :param task_id: Task id

        :rtype: dict
        :return: Dict
        """

        args = {"task_id": str(task_id)}

        return self._api_call("get", "task_log", args)

    def remove(self, task_id):
        """
        Remove task with the selected id

        :type task_id: str
        :param task_id: Task id

        :rtype: dict
        :return: Dict
        """

        args = {"task_id": str(task_id)}

        return self._api_call("get", "task_remove", args)

    def zombies(self):
        """
        Kill zombie tasks

        :rtype: dict
        :return: Task id
        """

        return self._api_call("get", "zombie")
