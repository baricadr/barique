import click
from barique.cli import pass_context, json_loads
from barique.decorators import custom_exception, None_output


@click.command('tree')
@click.argument("path", type=str)
@click.option(
    "--max_depth",
    help="Restrict to a max depth. Set to 0 for all files.",
    type=int
)
@pass_context
@custom_exception
@None_output
def cli(ctx, path, max_depth=0):
    """List files available from a remote repository for a local path as a tree

Output:

    None
    """
    return ctx.gi.file.tree(path, max_depth=max_depth)
