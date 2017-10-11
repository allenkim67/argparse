**argparse.py**

We want `_show_error` to do three things:

1. Show the proper usage.
2. Show what caused the error.
3. Exit the program

Showing the usage turned out to be very simple. Just import and reuse the one
in `help_menu.py`. The only change I made is, since `_usage` is being used
outside the `help_menu.py` file now, it should be considered a public function
so I dropped the leading underscore.

As for showing what caused the error, this was also simple. When we passed a
string to our custom exception class, we can print that message by passing
the error object itself to `print`.

Finally, it's considered good practice to limit the scope of your exception
handler as much as possible. Which is to say that if we use just a bare `except`
block, it will catch every possible error, even ones that we didn't intend. You
can see in our new code that now we only handle errors of type `ArgparseError`.
This is a new class, so let's take a look in the `exceptions.py` file.

**exceptions.py**

Here we can see `ArgparseError` subclasses `Exception`. But another change we've
made is that the previous classes `InvalidOptionalArgs` and `InvalidPositionalArgs`
subclass `ArgparseError`. This makes it so that our `except` block will catch
both `InvalidOptionalArgs` and `InvalidPositionalArgs`. This is because declaring
an exception class after `except` makes it so that it will catch exceptions
objects that come from either that class or a subclass of that class.

##### Follow Along

Now we can move on to the final function in our `argparse.py` file, the `_parse`
function. Try think about what this function does and how we can break it down
into simpler parts.