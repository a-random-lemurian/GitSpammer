from os import system
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

@app.command('branchstuffer')
@click.option('-b','--branch-count',help="Branches to create.",type=int)
@click.option('-c','--commit-count',help="Commits per branch.",type=int)
@click.option('--merge-branches-into',help="Merge all the branches when done.",type=str)
def branch_stuffer(branch_count, commit_count, merge_branches_into):
    branches = []
    for i in range(branch_count):
        branch_name = i
        branch_batch_id = get_letters(7)
        branches.append(f'{branch_name}-{branch_batch_id}')
        system(f'git branch {branch_name}-{branch_batch_id}')
        system(f'git switch {branch_name}-{branch_batch_id}')
        for i in range(commit_count):
            system(f'git commit -m "{i+1} of {commit_count} GitSpammer spam commit. {branch_batch_id}" --allow-empty')
        if merge_branches_into is not None:
            system(f'git switch {merge_branches_into}')
            for branch in branches:
                system(f'git merge {branch}')