This tutorial will teach you how to build a command line argument parser.

**argparse.py**

Our program will be based around a single `parse` function that gets passed a
`schema` dictionary. This dictionary should contain all the information about
how your command line options work. The `sys.argv` variable is a [list of
command line arguments passed by the user](https://stackoverflow.com/a/15606349/1817296).
We'll use this and the schema to output a dictionary with the parsed data.

Our program will have the following supported features:

1. `-h, --help` options show a generated help menu.

2. Incorrectly formed arguments will show an error.

3. Returns a dictionary of parsed arguments. Unpassed arguments will default to
False. If an arguments has both long and short names, it will default to the
long name.

Schema features:

1. `description` - String. Describes your whole program.

2. `optional_args` - List of optional arguments.

    1. `name` - String or list of strings. Either a long name with a `--` prefix
    or a short name with `-` prefix. If using both short and long names, they
    should be in a list. This property is required.

    2. `description` - String. Optional description of what this argument does.

    3. `param` - String. This indicates that a value should be passed.
    For example `--oarg=FOO`. By default, without `param` the argument will be
    set to a boolean.

    4. `required` - Boolean. This will cause an error if you don't include this argument.
    By default optional arguments are not required.

3. `positional_args` - List of position based arguments. Positional arguments
are matched in the order that they're declared, so order matters here!

    1. `name` - String. Should not have a `-` prefix. This property is required.

    2. `description` - String. Optional description of what this argument does.

    3. `n_args` - Integer or string. Optional property, defaults to 1. This
    indicates how many of this argument needs to be passed. Can be an integer or
    one of '*', '+', '?'. '*' indicates 0 or more. '+' indicates 1 or more.
    '?' indicates 0 or 1.

Unsupported features:

1. Schema validation - This tutorial will assume that the schema pass is
correctly formatted.

2. Optional argument assignment with spaces -  `=` must be used for both long and
short optional argument assignment. For example, `--oarg=FOO` or `-o=FOO`
instead of `-o FOO`.

3. Multiple variadic positional arguments - The special `n_args` '*', '+', '?'
can only be used once per schema. This is because having multiple of these
causes ambiguities in which argument should be assigned to which name.

4. Subcommands - This is when arguments are scoped to specific commands. For
example in git there are multiple commands like `commit`, `log`, `rebase`, each
with their own optional and positional arguments.

Unsuppored features are mainly because I wanted to keep this tutorial reasonably
short. However, implementing them would be a great exercise for readers once
they're done with the tutorial.

##### Follow Along

How would you start implementing the `parse` function? There are three main
features listed above. As a general rule if a feature would not fit in 5-10
lines of code I would create a new function for that feature.

##### References

[What does sys.argv[1] mean](https://stackoverflow.com/a/15606349/1817296)