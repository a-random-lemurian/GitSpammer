from os import system
from gitspammer.utils import get_letters
from gitspammer.entry import brancher as app
import click

@app.command('mk')
@click.option('-b','--branch-count',help='Number of branches.',default=0,type=int)
@click.option('-f','--force',help='Ignore confirmation dialogue and warnings.',is_flag=True)
def branchmaker(branch_count, force):
    if (
         branch_count is not None and
         branch_count > 30        and
         not force
       ):
        print(f'''
         ARE YOU SERIOUS?

        {branch_count} branches? That's a lot.

        Git might lag or even crash. This is why
        I have asked you to confirm this operation.

        Proceed at your own risk.
        ''')
        confirm = click.confirm('Please confirm')
        if not confirm:
            print('Cancelled. Better know what you\'re doing.')
            exit()
    for i in range(branch_count):
        make_git_branch(
                        return_list=False,
                        branch_batch_id=get_letters(7),
                        branch_name=i
                       )

# branchmaker is the CLI command access point,
# the actual git branching happens here so
# committer.py's branch commit stuffer can use
# this module too
def make_git_branch(return_list: bool, branch_batch_id, branch_name):
    system(f'git branch {branch_name}-{branch_batch_id}')