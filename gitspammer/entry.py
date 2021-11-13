# pylint: disable=unused-import, wrong-import-position, unnecessary-pass

import click

@click.group()
def cli():
    pass

@cli.group()
def brancher():
    """Create branches.
    """
    pass

@cli.group()
def committer():
    """Create and mess around with commits.
    """
    pass

import gitspammer.brancher
import gitspammer.committer
