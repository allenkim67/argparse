**argparse.py**

After some consideration, even `_usage` I think is too complex to fit in one
function. But now it's starting to feel like the help menu related code is
getting large enough that we'd want to move it into its own file.

**help_menu.py**

There's three parts to the usage message:

1. name of the program
2. optional argument usage
3. positional argument usage

Name of the program is simple enough to code directly, we can get it as the
first element in argv. So just have to pass that in from `parse` to `help_menu`
to `_usage`. Also note that we removed the `_` from help_menu because it is
considered a public method of the `help_menu.py` module.

##### Follow Along

Next we implement `_optional_args_usage`. Here's an example of the usage line
to refresh your memory. You can see all the possible optional arguments are
listed out separated by a space. You can see that some arguments have an
assigned value like `--oarg=FOO`. You can see that some arguments are inside
square brackets to indicate they're not required like `[--oarg]`. How would you
implement this function?