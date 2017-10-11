class ArgparseError(Exception):
    pass


class InvalidOptionalArgs(ArgparseError):
    pass


class InvalidPositionalArgs(ArgparseError):
    pass