#!/usr/bin/env python3
from safe_print_integer import safe_print_integer

for value in (42, -7, 0, "42", 3.5, [42]):
    print("Testing {!r}:".format(value))
    print("Returned: {}".format(safe_print_integer(value)))
