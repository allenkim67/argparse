**parser.py**

As I started writing this code I realized it was going to be long enough to
put in its own file.

This commit looks like a lot of code but most of it is straightforward.

In `parse` I decide to split the work into:

1. Parsing the optional arguments
2. Parsing the positional arguments

Each function gets passed only the relevant parts of the schema and `argv`.

In `_optional_args` I split the work into:

1. Passed arguments
2. Unpassed arguments, these should default to `False`.

In `_passed_o_args` I create a dictionary with the name of the argument as the
key, and the value is either True if there is no param, or the value of the
param if it exists. I created the function `_long_name` because I want to always
default to the long name, even if the user passed a short name.

To help build this function, I realized that I needed to find the optional
argument in the schema by the argument name. I remembered there was some code
in `validators.py` that does the same thing. It's good practice to reuse code
when you can so I moved this code into a new function called `find_o_arg_by_name`
in a new file called `schema_util.py`.

If you were wondering about the `**`, this is called dictionary unpacking and as
of python 3.5 you can use it to merge dictionaries.

##### Follow Along

Next try to implement `_unpassed_o_args`.

##### References

[How to merge two dictionaries in a single expression?](https://stackoverflow.com/questions/38987/how-to-merge-two-dictionaries-in-a-single-expression)