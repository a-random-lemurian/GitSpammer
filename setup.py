from setuptools import setup, find_packages
setup(
    name='GitSpammer',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'Click'
    ],
    entry_points={
        'console_scripts': [
            'gitspam = gitspammer.entry:cli'
        ],
    },
    description="Experiment with Git's features. Create as many test commits as necessary."
)