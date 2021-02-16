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
@click.option(
    "--dry_run",
    help="Do not make any pull, just list changes that would be made",
    is_flag=True
)
@pass_context
@custom_exception
@str_output
def cli(ctx, path, email="", dry_run=False):
    """Launch a pull task

Output:

    Id associated to the pull task
    """
    return ctx.gi.file.pull(path, email=email, dry_run=dry_run)
