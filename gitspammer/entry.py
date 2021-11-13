# pylint: disable=unused-import, wrong-import-position, unnecessary-pass

import click

@click.group()
def cli():
    pass

@cli.group()
def brancher():
    pass

@cli.group()
def committer():
    pass

import gitspammer.brancher
import gitspammer.committer