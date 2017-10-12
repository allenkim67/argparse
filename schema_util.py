def find_o_arg_by_name(schema_o_args, name):
    for o_arg in schema_o_args:
        match_str = isinstance(o_arg['name'], str) and name == o_arg['name']
        match_list = isinstance(o_arg['name'], list) and name in o_arg['name']
        if match_str or match_list:
            return o_arg
    return None