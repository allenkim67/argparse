def help_menu(schema, prog):
    parts = [_usage(schema, prog),
             schema.get('description'),
             _positional_args(schema),
             _optional_args(schema)]

    return '\n\n'.join([p for p in parts if p])


def _usage(schema, prog):
    args = ' '.join([_optional_args_usage(schema['optional_args']),
                     _positional_args_usage(schema['positional_args'])])
    return f'usage: {prog} {args}'


def _optional_args_usage(o_args):
    pass


def _positional_args_usage(p_args):
    pass


def _positional_args(schema):
    pass


def _optional_args(schema):
    pass
