import click
from barique.commands.task.show import cli as show


@click.group()
def cli():
    """
    Track progress of Baricadr tasks
    """
    pass


cli.add_command(show)
