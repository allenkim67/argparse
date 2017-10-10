**argparse.py**

Our help menu has 4 parts:

1. Usage
2. Description
3. Positional Arguments
4. Optional Arguments

Description is simple enough to code directly, just get it from the schema. The
other 3 parts are too complex so we create new functions for them. It's possible
that the schema won't have a description or positional arguments (optional
arguments will have at least --help), so we use the `if p` part of the list
comprehension to keep only the parts that exist and put join the parts with an
empty line.

##### Follow Along

We'll need to implement our new methods, starting with `_usage`. Remember that
usage looks like this. Do you think `_usage` can fit in one function? If not
how would you break it up?