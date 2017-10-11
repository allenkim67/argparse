**help_menu.py**

The `_positional_args` function relatively straightforward. If there are no
positional arguments then we return None. This will allow it to get filtered out
in the `help_menu` function. Otherwise we show the header as "positional arguments"
and then list the names and descriptions. We join with "\n" which mean new line,
and separate the listing with "\t\t" which mean two tabs.

##### Follow Along

Let's move on to `_optional_args` function. Remember this determines what is
shown in the help menu for the "optional arguments" portion. In should be the
same as the `_positional_args` function except for the name part. How would
you approach this function?
