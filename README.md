# Baricadr client

A Python library and CLI for interacting with a (Baricadr)[https://github.com/baricadr/baricadr] server.

## Installation

```bash
$ pip install baricadr   # Not ready yet

# On first use you'll need to create a config file to connect to the server, just run:

$ barique init
```

This will create a barique config file in ~/.barique.yml

## Examples

```bash

# List files in a remote repository
$ barique file list /repos/test_repo/
[
    "file.txt",
    "file2.txt"
]

# Ask Baricadr to pull a single file
$ barique file pull /repos/test_repo/file.txt
7958b29c-2a14-486c-90f0-585e68ac9f44

# Check the status of a pull task
$ barique task show 7958b29c-2a14-486c-90f0-585e68ac9f44
{
    "error": "false",
    "finished": "true",
    "info": null
}

```

## License

Available under the MIT License
