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
from validators import validate_argv


def parse(schema):
    argv = sys.argv

    if len(argv) == 2 and argv[1] in ['-h', '--help']:
        _show_help(schema)

    try:
        validate_argv(schema, argv)
    except:
        _show_error()

    return _parse(schema, argv)


def _show_help(schema):
    parts = [_usage(schema),
             schema.get('description'),
             _positional_args(schema),
             _optional_args(schema)]

    return '\n\n'.join([p for p in parts if p])


def _usage(schema):
    pass


def _positional_args(schema):
    pass


def _optional_args(schema):
    pass


def _show_error():
    pass


def _parse(schema, argv):
    pass
