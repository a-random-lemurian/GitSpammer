# GitSpammer
GitSpammer is a Python application for creating empty Git commits and branches. If you need to ask why you would want this, see the `Intended uses` section.

# Install
Mac/Linux/Unix-like: Copy-paste these commands into a directory of your choice.
```
git clone https://github.com/a-random-lemurian/GitSpammer.git
cd GitSpammer
pip install --editable .
```

# Commands
## `gitspam committer`
### `commit`
`gitspam committer commit -c [INTEGER]`
Create fake commits. After the `-c` flag place the number of commits that you want to make.
### `branchstuffer`
`gitspam committer branchstuffer -b [BC] -c [BC]`
Create several branches and then stuff them with fake commits.

Contains a long flag called `--merge-branches-into`. After the flag, input the name of any branch you wish to merge the fake branches with.

# Intended uses
- Create fake commits, fake branches structured just like your actual Git repository to test out a command you think is too risky to blindly perform on your real repository.
- Play around with Git commands.

## But please don't use me for:
- Spamming actual repositories (that's not nice).

# Disclaimer
GitSpammer is **not associated in any way with the maintainers of the Git source control management system.** GitSpammer is a tool intended for experimentation with Git. The intended use of the tool is listed in `Intended uses`.