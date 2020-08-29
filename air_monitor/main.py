#!/usr/bin/env python3
import sys
import click

"""
    Endpoint to AliceAir
"""

from air_monitor.utils import logger

# import commands
from air_monitor.routes.serve import serve


@click.group()
@click.pass_context
def cli(ctx):
    ctx.ensure_object(dict)


# include cli commands
cli.add_command(serve)


def main():
    """
        Before command routing initialize global objects.
        :return: int - exit status
    """
    debug = False
    if '--debug' in sys.argv:
        sys.argv.remove('--debug')
        log = logger.init(debug=True)
        debug = True
    else:
        log = logger.init()

    sys.exit(cli(obj={"debug": debug}))


if __name__ == '__main__':
    main()