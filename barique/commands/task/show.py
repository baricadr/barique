import click
from barique.cli import pass_context, json_loads
from barique.decorators import custom_exception, dict_output


@click.command('show')
@click.argument("task_id", type=str)
@pass_context
@custom_exception
@dict_output
def cli(ctx, task_id):
    """Show task with the selected id

Output:

    Dict
    """
    return ctx.gi.task.show(task_id)
