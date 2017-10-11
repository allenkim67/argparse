**validators.py**

I've broken down the validator into the following cases:

1. Passing an argument that you weren't supposed to
2. Not passing an argument that you were supposed to

These cases apply to both positional and optional arguments, so we end up with
four cases total. There are probably other ways to break this function
up that would also make sense, but this seems like it should cover all error
cases. We can move forward like this and make changes if we need to.

##### Follow Along

Now we need to implement our new functions. We can start with
`_no_invalid_o_args`. What would be considered an invalid optional argument?
What do we do once we've identified an invalid optional argument?