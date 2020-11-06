import click
from barique.cli import pass_context, json_loads
from barique.decorators import custom_exception, dict_output


@click.command('zombies')
@pass_context
@custom_exception
@dict_output
def cli(ctx):
    """Kill zombie tasks

Output:

    Task id
    """
    return ctx.gi.task.zombies()
