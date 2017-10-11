**validators.py**

To implement `_no_invalid_o_args` we need to:

1. Get a list of only the optional arguments, with positional arguments removed.
2. Check each argument to see if it's valid.

Here are the requirements for a valid optional argument:

1. The name of the argument must be in the schema.
2. If there is a `param` property, there should be value assigned.
3. If there is no `param` property, there should be no value assigned.

I've added a convenience function `_find_o_arg_by_name`. In order to check if an
argument is valid we use its name and try to look it up in the schema.

I've also create a new subclass of `Exception` called `InvalidOptionalArgs`. When
we find an invalid argument we can raise this exception with the `raise` keyword.
What does this do? If you look inside `argparse.py`, you can see that we call
`validate_argv` inside a `try` block. That means any time an exception is raised
during the execution of `validate_argv` the code will immediately jump into the
`except` block.

What is the benefit of doing things this way?

The main benefit is that no matter where you are in the execution of a `try`
block, any raised exception will immediately jump you to the `except` block.
Think about how you would do this without `try` and `except`.

Another benefit is that by subclassing
`Exception` we can get access to a stacktrace from when the error occured (although
we won't be using this in our project). This is just one of the features of the
`Exception` class which is a built-in class.

Because exceptions are usually checked by their class name all we have to do is
subclass `Exception` and `pass` in the body. This is a common pattern, but you
could also add things in the body, for example a logger to log when this error
is raised.

Later we'll see that we can access the error object in the `except` block and
from there we can access the error message.

##### Follow Along

Next let's move on to `_no_invalid_p_args`. This one is a little bit trickier.
How do we know whether a positional argument is invalid or not? What are the
different cases of invalid argument?


##### References

[Python 3 Docs: Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)