from os import system
import json
from gitspammer.utils import get_letters
from gitspammer.entry import committer as app
import click


@app.command('commit')
@click.option('-c','--commitcount',help="How many commits to make.",default=10)
def mkcommit(commitcount):
    commitid = get_letters() # get a commit id to prevent
                             # duplicate messages later on
    filename = 'GITSPAMMERFILE'
    for i in range(commitcount):
        jsondata = {'GitSpam': get_letters()}
        json.dump(jsondata,open('GITSPAMMERFILE','w'))
        system(f'git add GITSPAMMERFILE && git commit -m "{i+1} of {commitcount} GitSpammer modified GITSPAMMERFILE. {commitid}"')
