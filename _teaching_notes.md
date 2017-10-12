**parser.py**

In `_unpassed_o_args` we want to get all the optional argument names in the user
passed command line arguments. Then we want to find the arguments in the schema
that weren't passed. We set these values to False.

Again we use many of the same tricks in the previous commits, like split on '='
and normalizing the argument name to a list.

##### Follow Along

We're almost done, the last function we need to implement is `_positional_args`.
The tricky part of this function is to handle the variadic arguments
(n_args equal to '*' or '+'). We would need to first parse out the non-variadic
arguments, and then we can assign the remaining arguments to the variadic argument.