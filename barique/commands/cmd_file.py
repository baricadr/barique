import click
from barique.commands.file.freeze import cli as freeze
from barique.commands.file.list import cli as list
from barique.commands.file.pull import cli as pull
from barique.commands.file.tree import cli as tree


@click.group()
def cli():
    """
    Manipulate files managed by Baricadr
    """
    pass


cli.add_command(freeze)
cli.add_command(list)
cli.add_command(pull)
cli.add_command(tree)
