import click
from barique.commands.task.list import cli as list
from barique.commands.task.log import cli as log
from barique.commands.task.remove import cli as remove
from barique.commands.task.show import cli as show
from barique.commands.task.zombies import cli as zombies


@click.group()
def cli():
    """
    Track progress of Baricadr tasks
    """
    pass


cli.add_command(list)
cli.add_command(log)
cli.add_command(remove)
cli.add_command(show)
cli.add_command(zombies)
