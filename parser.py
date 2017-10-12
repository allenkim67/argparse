from schema_util import find_o_arg_by_name


def parse(schema, argv):
    schema_o_args = schema.get('optional_args') or []
    schema_p_args = schema.get('positional_args') or []
    o_argv = [a for a in argv if a.startswith('-')]
    p_argv = [a for a in argv if not a.startswith('-')]

    return {**_optional_args(schema_o_args, o_argv),
            **_positional_args(schema_p_args, p_argv)}


def _optional_args(schema_o_args, argv):
    return {**_passed_o_args(schema_o_args, argv),
            **_unpassed_o_args(schema_o_args, argv)}


def _long_name(schema_o_args, arg_name):
    o_arg = find_o_arg_by_name(schema_o_args, arg_name)
    name = o_arg['name']
    return sorted(name)[0] if isinstance(name, list) else name


def _passed_o_args(schema_o_args, argv):
    o_argv = [a.split('=') for a in argv]
    return {_long_name(schema_o_args, a[0]): a[1] if len(a) > 1 else True
            for a in o_argv}


def _unpassed_o_args(schema_o_args, argv):
    pass


def _positional_args(schema, argv):
    pass
