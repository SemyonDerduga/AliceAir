import click
from air_monitor.actions.serve import run

"""
    Main command for serve skill.
"""

HELP_PORT = 'Skill server port, default 5555.'


@click.command()
@click.pass_context
@click.option('-p', '--port', type=int, default=5555, help=HELP_PORT)
def serve(ctx, port):
    """
        Serve skill server.
    """
    run(ctx, port)
