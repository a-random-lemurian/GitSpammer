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