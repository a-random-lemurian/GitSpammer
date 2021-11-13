from os import system
import json
from gitspammer.utils import get_letters
from gitspammer.entry import committer as app
import click


@app.command('commit')
@click.option('-c','--commitcount',help="How many commits to make.",default=10)
def mkcommit(commitcount):
    commitid = get_letters(8) # get a commit id to prevent
                             # duplicate messages later on
    for i in range(commitcount):
        system(f'git commit -m "{i+1} of {commitcount} GitSpammer spam commit. {commitid}" --allow-empty')
