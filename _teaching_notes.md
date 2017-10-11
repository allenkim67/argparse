**validators.py**

In `_required_o_args_exist` we just need to loop through the schema's optional
arguments that have a `required` property as `True` and see if it's name is in
the list of command line arguments passed by the user.

There's only two tricky parts to this:

1. The user passed optional arguments might look like this: `--oarg=FOO` when
we really just want the part before the `=`. We can do this by splitting on
`=` and taking the first element. This will work even if there is no `=` in the
string.

2. Once we have the argument name we can search through the schema, but we have
to take into account that some optional argument's name property can be either
a list or a string. I get around this problem by putting the string in a list if
name is a string. Then I can just check for membership in that list.

##### Follow Along

With that, we're done with the validation functions. If there is an error in the
command line arguments passed by the user we should see an exception get raised.
Now we can go back to `argparse.py` and finish our `show_error` function. One
hint I'll give is that we want to show the proper usage in our error message
and we already have a function for that in `help_menu.py`. Can we reuse this
function?