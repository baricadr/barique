import click
from barique.cli import pass_context, json_loads
from barique.decorators import custom_exception, str_output


@click.command('pull')
@click.argument("path", type=str)
@click.option(
    "--email",
    help="User email adress for notification",
    type=str
)
@pass_context
@custom_exception
@str_output
def cli(ctx, path, email=""):
    """Launch a pull task

Output:

    Id associated to the pull task
    """
    return ctx.gi.file.pull(path, email=email)
