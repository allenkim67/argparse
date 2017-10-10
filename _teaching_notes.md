**help_menu.py**

When implementing `_optional_args_usage`:

1. We want to loop through each optional argument in the schema.
2. For each argument we want to get the name. If there's a short and long name,
then we want to default to the short name.
3. If there's a `param` property we want to add an `=` and the name of the param
in all-caps.
4. Unless the property is required, we want to wrap it in square brackets.
5. We want to join each argument into a single string separated by a space.

Finally we've reached a point where we can code everything without creating new
functions. If you read the code carefully you'll see that our code follows the
above requirements quite closely.

##### Follow Along

Next let's go back to the `_positional_args_usage` function. Let's look at the
usage example again. For positional args we can see a list of all-caps names.
The formatting of these arguments will depend on the `n_args` property from the
schema.

If the property is not set `n_args` defaults to 1, so if n_args is an integer
we repeat that argument `n_arg` times. But if it's one of `'*'`, `'+'`, or `'?'`
then it needs to be handled differently. Remember, `'*'` means 0 or more,
`'+'` means 1 or more, `'?'` means 1 or 0.

Square brackets indicate the argument is optional. `...` indicates 0 or more of
that argument. So for `'*'` we can use `...`. For '?' we can use square brackets.
For `'+'` we can use a combination of both like this: PARG [PARG...].

##### References

[What's the canonical way to check for type in python?](https://stackoverflow.com/questions/152580/whats-the-canonical-way-to-check-for-type-in-python)
