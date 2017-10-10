**argparse.py**

As mentioned we want our `parse` function to do three things:

1. If passed an -h or --help command we want to show a help menu.
2. If we get incorrectly formatted input we should show an error and usage message.
3. Otherwise we should return the parsed data.

Checking if -h or --help command is simple enough to code in directly, but
everything else is complex enough that we'll want to create new functions. By
creating new functions with good names it becomes easy to see what we intend the
`parse` function to do. It also allows us to break a larger problem down into
simpler problems.

You might be wondering why we have function names that start with a `_`. This is
to distinguish between private and public variables. If we imagine that someone
is going to be using our argparse module, then `parse` is really the only
function that we want them to use. The private functions aren't intended to be
used by the public so they're marked with the `_` prefix.

If you don't know how `try` and `except`, you should have a better idea by the
end of this tutorial.

##### Follow Along

We need to implement our new functions. We'll start at the top with the
`_show_help` function. The help menu should look like this. I recommend breaking
up the help menu into parts. What would the parts be and how would you code it?

##### References
