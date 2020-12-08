import click
from barique.cli import pass_context, json_loads
from barique.decorators import custom_exception, dict_output


@click.command('remove')
@click.argument("task_id", type=str)
@pass_context
@custom_exception
@dict_output
def cli(ctx, task_id):
    """Remove task with the selected id

Output:

    Dict
    """
    return ctx.gi.task.remove(task_id)
