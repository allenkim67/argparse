from exceptions import InvalidOptionalArgs


def validate_argv(schema, argv):
    _no_invalid_o_args(schema, argv)
    _no_invalid_p_args()
    _required_o_args_exist()
    _required_p_args_exist()


def _find_o_arg_by_name(schema, name):
    o_args = schema.get('optional_args') or []
    for o_arg in o_args:
        match_str = isinstance(o_arg['name'], str) and name == o_arg['name']
        match_list = isinstance(o_arg['name'], list) and name in o_arg['name']
        if match_str or match_list:
            return o_arg
    return None


def _no_invalid_o_args(schema, argv):
    for arg in [a for a in argv if a.startswith('-')]:
        name = arg.split('=')[0]
        o_arg = _find_o_arg_by_name(schema, name)

        if not o_arg:
            raise InvalidOptionalArgs(f'Optional Argument "{arg}" does not exist')
        if o_arg.get('param') and len(arg.split('=')) < 2:
            raise InvalidOptionalArgs(f'Optional Argument "{name}" requires parameter {o_arg["param"]}')
        if not o_arg.get('param') and len(arg.split('=')) > 1:
            raise InvalidOptionalArgs(f'Optional Argument "{name}" should have no parameter')


def _no_invalid_p_args():
    pass


def _required_o_args_exist():
    pass


def _required_p_args_exist():
    pass