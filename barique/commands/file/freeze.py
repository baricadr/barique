import click
from barique.cli import pass_context, json_loads
from barique.decorators import custom_exception, str_output


@click.command('freeze')
@click.argument("path", type=str)
@click.option(
    "--force",
    help="Force freezing, even if the freezing delay was not reached",
    is_flag=True
)
@click.option(
    "--dry_run",
    help="Do not make any deletion, just list changes that would be made",
    is_flag=True
)
@click.option(
    "--email",
    help="User email adress for notification",
    type=str
)
@pass_context
@custom_exception
@str_output
def cli(ctx, path, force=False, dry_run=False, email=""):
    """Launch a freeze task

Output:

    Id associated to the freeze task
    """
    return ctx.gi.file.freeze(path, force=force, dry_run=dry_run, email=email)
