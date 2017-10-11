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
    o_args_usage = []

    for o_arg in o_args:
        if isinstance(o_arg['name'], str):
            arg_str = o_arg['name']
        elif isinstance(o_arg['name'], list):
            arg_str = sorted(o_arg['name'])[1]

        if o_arg.get('param'):
            arg_str = f'{arg_str}={o_arg["param"].upper()}'

        if not o_arg.get('required'):
            arg_str = f'[{arg_str}]'

        o_args_usage.append(arg_str)

    return ' '.join(o_args_usage)


def _positional_args_usage(p_args):
    return ' '.join([_p_arg_usage(p_arg) for p_arg in p_args])


def _p_arg_usage(p_arg):
    name = p_arg['name'].upper()

    if not p_arg.get('n_args'):
        return name
    else:
        if p_arg['n_args'] == '?':
            return f'[{name}]'
        elif p_arg['n_args'] == '*':
            return f'[{name}...]'
        elif p_arg['n_args'] == '+':
            return f'{name} [{name}...]'
        else:
            return ' '.join([name] * p_arg['n_args'])


def _positional_args(schema):
    pass


def _optional_args(schema):
    pass
