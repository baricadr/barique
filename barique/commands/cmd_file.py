import click
from barique.commands.file.list import cli as list
from barique.commands.file.pull import cli as pull


@click.group()
def cli():
    pass


cli.add_command(list)
cli.add_command(pull)
