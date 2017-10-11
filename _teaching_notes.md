**validators.py**

After some thought, there's two ways to cause an error with positional arguments:

1. pass too many arguments
2. pass too few arguments

So I've create new functions `_under_max_p_args` and `_over_min_p_args` accordingly.

For `_under_max_p_args`:

1. If there is any n_arg equal to '*' or '+' then there can be no maximum, so
just return.

2. Otherwise calculate the maximum arguments. So `max_args` is the sum of all
`n_args` where no `n_arg` property defaults to 1, and '?' will be at most 1.

3. If the number of passed positional arguments is greater than the max, raise
`InvalidPositionalArgs` error. This is also a subclass of `Exception`.

For `_over_min_p_args`:

1. Calculate the minimum number of arguments required. '*' and '?' can both be
zero so they don't increase the minimum. So `min_args` is the sum of all `n_args`
where no `n_arg` property defaults to 1 and '+' requires at least 1.

2. If the number of passed positional arguments is less than the minimum, raise
`InvalidPositionalArgs` error.

At this point I realized that this covers all error cases related to positional
arguments so I removed the `_required_p_args_exist` function.

##### Follow Along

The last method in our validator is `_required_o_args_exist`. We need to look
through all the required optional arguments and see if any of them are missing.