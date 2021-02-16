import click
from barique.cli import pass_context, json_loads
from barique.decorators import custom_exception, dict_output


@click.command('log')
@click.argument("task_id", type=str)
@pass_context
@custom_exception
@dict_output
def cli(ctx, task_id):
    """Show log from the task with the specified id

Output:

    Dict
    """
    return ctx.gi.task.log(task_id)
