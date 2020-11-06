import click
from barique.cli import pass_context, json_loads
from barique.decorators import custom_exception, list_output


@click.command('list')
@pass_context
@custom_exception
@list_output
def cli(ctx):
    """List recent tasks

Output:

    List of tasks
    """
    return ctx.gi.task.list()
