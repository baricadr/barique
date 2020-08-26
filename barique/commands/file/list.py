import click
from barique.cli import pass_context, json_loads
from barique.decorators import custom_exception, list_output


@click.command('list')
@click.argument("path", type=str)
@click.option(
    "--compare",
    help="Only list files missing from the local path",
    is_flag=True
)
@pass_context
@custom_exception
@list_output
def cli(ctx, path, compare=False):
    """List files available from a remote repository for a local path

Output:

    List of file relative paths
    """
    return ctx.gi.file.list(path, compare=compare)
