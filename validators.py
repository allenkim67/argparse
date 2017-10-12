from exceptions import InvalidOptionalArgs, InvalidPositionalArgs
from schema_util import find_o_arg_by_name


def validate_argv(schema, argv):
    _no_invalid_o_args(schema, argv)
    _no_invalid_p_args(schema, argv)
    _required_o_args_exist(schema, argv)


def _no_invalid_o_args(schema, argv):
    for arg in [a for a in argv if a.startswith('-')]:
        schema_o_args = schema.get('optional_args') or []
        name = arg.split('=')[0]
        o_arg = find_o_arg_by_name(schema_o_args, name)

        if not o_arg:
            raise InvalidOptionalArgs(f'Optional Argument "{arg}" does not exist')
        if o_arg.get('param') and len(arg.split('=')) < 2:
            raise InvalidOptionalArgs(f'Optional Argument "{name}" requires parameter {o_arg["param"]}')
        if not o_arg.get('param') and len(arg.split('=')) > 1:
            raise InvalidOptionalArgs(f'Optional Argument "{name}" should have no parameter')


def _no_invalid_p_args(schema, argv):
    p_args = [a for a in argv[1:] if not a.startswith('-')]
    schema_p_args = schema.get('positional_args') or []

    _under_max_p_args(schema_p_args, p_args)
    _over_min_p_args(schema_p_args, p_args)


def _under_max_p_args(schema_p_args, p_args):
    if any(a.get('n_args') in ['*', '+'] for a in schema_p_args): return

    max_args = sum([1 if a.get('n_args') in [None, '?'] else a['n_args']
                    for a in schema_p_args])

    if len(p_args) > max_args:
        raise InvalidPositionalArgs(f'Too many positional arguments')


def _over_min_p_args(schema_p_args, p_args):
    min_args = sum([1 if a.get('n_args') in [None, '+'] else a['n_args']
                    for a in schema_p_args
                    if not a.get('n_args') in ['*', '?']])

    if len(p_args) < min_args:
        raise InvalidPositionalArgs(f'Missing one or more required positional arguments')


def _required_o_args_exist(schema, argv):
    o_args = schema.get('optional_args') or []
    argv_names = [a.split('=')[0] for a in argv]
    for o_arg in [a for a in o_args if a.get('required')]:
        n = o_arg['name']
        names = n if isinstance(n, list) else [n]
        if not any(name in argv_names for name in names):
            raise InvalidOptionalArgs(f'Optional arg "{sorted(names)[0]}" is required')