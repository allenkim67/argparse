**help_menu.py**

The `_positional_args_usage` function is very similar to the previous function
`_optional_args_usage` except with different rules for formatting each argument.
In this case it depends mostly on its `n_args` property:

1. If `n_args` is not set, then default to showing the name once.
2. If `n_args` is '?' wrap in square brackets.
3. If `n_args` is '*' wrap in square brackets and add `...`.
4. If `n_args` is '+' show the name once and then wrap in square brackets and then add `...`.
5. If `n_args` is a number then show name that many times.

Another difference here compared to `_optional_args_usage` is that I've chosen
to add a second function. One function handles looping and joining, and another
is used during each iteration. Try comparing with `_optional_args_usage` and see
that both approaches do about the same thing.

You also might be wondering what it means to multiply a list by a number. Multiplying
a list is the same as appending a list to itself that many times. For example:

```
[1, 2, 3] * 3 == [1, 2, 3, 1, 2, 3, 1, 2, 3]
```

##### Follow Along

Now let's go back and add the `_positional_args` function which adds that part
into the help menu. Here's a reminder of what that part looks like. You can see
it's just a header and a listing of the name of the positional argument and its
description.
