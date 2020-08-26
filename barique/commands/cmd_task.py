import click
from barique.commands.task.show import cli as show


@click.group()
def cli():
    pass


cli.add_command(show)
