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
import parser
from validators import validate_argv
from exceptions import ArgparseError
from help_menu import help_menu, usage


def parse(schema):
    argv = sys.argv

    if len(argv) == 2 and argv[1] in ['-h', '--help']:
        _show_help(schema, argv[0])

    try:
        validate_argv(schema, argv)
    except ArgparseError as e:
        _show_error(e, schema, argv[0])

    return parser.parse(schema, argv)


def _show_help(schema, prog):
    print(help_menu(schema, prog))
    sys.exit()


def _show_error(error, schema, prog):
    print(usage(schema, prog))
    print(f'{prog}: error: {error}')
    sys.exit()

