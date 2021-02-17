# Barique

![Lint](https://github.com/baricadr/barique/workflows/Lint/badge.svg?branch=master)
[![Documentation](https://readthedocs.org/projects/barique/badge/?version=latest)](http://barique.readthedocs.io/en/latest/?badge=latest)

A Python client (library and CLI) for interacting with a [Baricadr](https://github.com/baricadr/baricadr) server.

## Installation

```bash
$ pip install barique

# On first use you'll need to create a config file to connect to the server, just run:

$ barique init
Welcome to Barique
Baricadr server host: localhost
Baricadr server port: 9100
Is your Baricadr instance running behind an authentication proxy? [y/N]: n
Testing connection...
Ok! Everything looks good.
Ready to go! Type `barique` to get a list of commands you can execute.

```

This will create a barique config file in ~/.barique.yml

## Examples

```bash

# List files in a remote repository
$ barique file list /repos/test_repo/
[
    {
        "Path": "file.txt"
    },
    {
        "Path": "file2.txt"
    }
]

# Ask Baricadr to pull a single file
$ barique file pull /repos/test_repo/file.txt
7958b29c-2a14-486c-90f0-585e68ac9f44

# Check the status of a pull task
$ barique task show 7958b29c-2a14-486c-90f0-585e68ac9f44
{
    "created": "Wed, 17 Feb 2021 15:11:56 GMT",
    "error": null,
    "finished": "Wed, 17 Feb 2021 15:12:03 GMT",
    "path": "/repos/test_repo/file.txt",
    "started": "Wed, 17 Feb 2021 15:11:58 GMT",
    "status": "finished",
    "task_id": "7958b29c-2a14-486c-90f0-585e68ac9f44",
    "type": "pull"
}

# Ask Baricadr to freze a single file
$ barique file freeze /repos/test_repo/file2.txt
7958b29c-2a14-486c-90f0-585e68ac9f44

# Check the status of a pull task
$ barique task show 7958b29c-2a14-486c-90f0-585e68ac9f44
{
    "created": "Wed, 17 Feb 2021 15:16:49 GMT",
    "error": null,
    "finished": "Wed, 17 Feb 2021 15:16:52 GMT",
    "path": "/repos/test_repo/file2.txt",
    "started": "Wed, 17 Feb 2021 15:16:51 GMT",
    "status": "finished",
    "task_id": "7958b29c-2a14-486c-90f0-585e68ac9f44",
    "type": "freeze"
}
```

## License

Available under the MIT License
