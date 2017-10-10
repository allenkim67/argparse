"""
Example schema:

schema = {
    'description': 'This is a project description',
    'optional_args': [
        {
            'name': ['--verbose', '-v'],
            'description': 'show verbose output',
        },
        {
            'name': '--config',
            'description': 'path to config file',
            'param': 'path'
        }
    ],
    'positional_args': [
        {
            'name': 'filename',
            'description': 'name of file',
            'n_args': '+'
        }
    ]
}
"""


import sys


def parse(schema):
    argv = sys.argv
    pass
