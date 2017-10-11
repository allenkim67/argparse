**help_menu.py**

For `_optional_args` we need to:

1. Add the `-h, --help` argument. Remember this is an argument that we add in
for the user.
2. Return the header and a listing of optional arguments each on a new line.

To generate each line I created the new function `_o_arg_and_description` which:
1. Checks if the name is a string or a list.
2. Generates the name portion (this happens in `_o_arg_and_param`)
3. Adds the description portion.

In `_o_arg_and_param` we add the param to the name if it exists.

This commit looks like a lot of code, but try reading carefully and you'll find
that what it's doing is relatively simple.

##### Follow Along

That was the last function in `help_menu.py`. Returning to `argparse.py` we can
see that first we try to validate the user's arguments, and if an exception
occurs we show an error message. So the first thing we need to do is implement
our `validate_argv` function in `validators.py`.

Take a moment to consider what are the possible error cases.