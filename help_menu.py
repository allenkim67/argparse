def help_menu(schema, prog):
    parts = [usage(schema, prog),
             schema.get('description'),
             _positional_args(schema),
             _optional_args(schema)]

    return '\n\n'.join([p for p in parts if p])


def usage(schema, prog):
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
    p_args = schema.get('positional_args')

    if not p_args or len(p_args) == 0: return None

    p_args_str = '\n'.join([f'{arg["name"].upper()}\t\t{arg.get("description")}'
                            for arg in p_args])

    return f'positional arguments:\n{p_args_str}'


def _optional_args(schema):
    o_args = _add_help_arg(schema['optional_args'])
    o_args_str = '\n'.join([_o_arg_and_description(o_arg) for o_arg in o_args])
    return f'optional arguments:\n{o_args_str}'


def _add_help_arg(schema_o_args):
    help_arg = {'name': ['-h', '--help'],
                'description': 'show this help message and exit'}
    return [help_arg, *schema_o_args]


def _o_arg_and_description(o_arg):
    if isinstance(o_arg['name'], str):
        o_arg_str = _o_arg_and_param(o_arg['name'], o_arg)

    elif isinstance(o_arg['name'], list):
        o_arg_str = ', '.join(_o_arg_and_param(name, o_arg)
                              for name in o_arg['name'])

    return f'{o_arg_str}\t\t{o_arg.get("description")}'


def _o_arg_and_param(name, o_arg):
    if o_arg.get('param'):
        return f'{name}={o_arg["param"].upper()}'
    else:
        return name
