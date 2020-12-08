import click
from barique.cli import pass_context, json_loads
from barique.decorators import custom_exception, list_output


@click.command('list')
@click.argument("path", type=str)
@click.option(
    "--full",
    help="List full information for each file (size (in bytes), mtime, etc..)",
    is_flag=True
)
@click.option(
    "--missing",
    help="Only list files missing from the local path",
    is_flag=True
)
@click.option(
    "--max_depth",
    help="Restrict to a max depth. Set to 0 for all files.",
    default="1",
    show_default=True,
    type=int
)
@click.option(
    "--from_root",
    help="Return full paths from root of the repo (instead of relative to given path)",
    is_flag=True
)
@pass_context
@custom_exception
@list_output
def cli(ctx, path, full=False, missing=False, max_depth=1, from_root=False):
    """List files available from a remote repository for a local path

Output:

    List of file relative paths
    """
    return ctx.gi.file.list(path, full=full, missing=missing, max_depth=max_depth, from_root=from_root)
