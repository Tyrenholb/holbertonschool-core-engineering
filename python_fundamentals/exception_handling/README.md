# Python - Exception Handling

Six functions practise handling selected runtime errors and raising exceptions.
The exercises combine formatting, bounded list access, division, return values,
and a `finally` block that reports the division result.

## General requirements

- Correction environment: Ubuntu 20.04 LTS with Python 3.8.x.
- Every Python file must start exactly with `#!/usr/bin/env python3`.
- Python files must be executable and end with a newline.
- Code must follow PEP8, checked with pycodestyle 2.7.x.
- Output formatting must match the expected results exactly.
- External libraries are not allowed unless explicitly required by the task.

These exercises use no external runtime libraries.

## Functions

| File | Behavior |
| --- | --- |
| [`safe_print_list.py`](safe_print_list.py) | Prints up to `x` indexed items with no separators, stops on `IndexError`, adds a newline, and returns the number printed |
| [`safe_print_integer.py`](safe_print_integer.py) | Prints an integer-formattable value and returns `True`; catches `TypeError`/`ValueError` and returns `False` without printing on failure |
| [`safe_print_list_integers.py`](safe_print_list_integers.py) | Examines the first `x` positions, skips values that fail integer formatting, prints a newline, and returns the printed count |
| [`safe_print_division.py`](safe_print_division.py) | Divides two values, catches `TypeError`/`ValueError`/`ZeroDivisionError`, prints the result from `finally`, and returns that result or `None` |
| [`raise_exception.py`](raise_exception.py) | Raises `TypeError` without a message |
| [`raise_exception_msg.py`](raise_exception_msg.py) | Raises `NameError` with the supplied message |

## Usage

These files define functions without a standalone caller. From the repository
root:

```bash
cd python_fundamentals/exception_handling
python3 -B - <<'PYTHON'
from safe_print_list import safe_print_list
from safe_print_integer import safe_print_integer
from safe_print_division import safe_print_division

print(safe_print_list([1, 2], 4))
print(safe_print_integer("bad"))
print(safe_print_division(10, 2))
print(safe_print_division(10, 0))
PYTHON
```

Output:

```text
12
2
False
Inside result: 5.0
5.0
Inside result: None
None
```

`12` is the concatenated list output, not the number twelve returned by the
function. The following `2` is its printed count. Division uses `/`, so the
successful result is the floating-point value `5.0`.

To catch a deliberately raised exception:

```bash
python3 -B - <<'PYTHON'
from raise_exception_msg import raise_exception_msg

try:
    raise_exception_msg("problem")
except NameError as error:
    print(error)
PYTHON
```

It prints `problem`. Without the caller's handler, the exception propagates
and Python displays a traceback.

## Error-handling limits

- `safe_print_list` stops when the requested position is beyond the list.
  It catches `IndexError`, not every possible access or formatting error.
- `safe_print_list_integers` catches bad formatting but does not catch
  `IndexError`. Requesting more positions than exist can therefore raise.
- Printing multiple list items adds no spaces or commas. Exact output and
  final newline behavior matter independently of the returned counts.
- `safe_print_integer` uses `{:d}` formatting rather than converting numeric
  strings. A string such as `"12"` is not accepted as the integer `12`.
- The handlers are specific; they do not provide general validation for
  arbitrary custom objects or every exception type.

The examples, explicit exception types/messages, and the difference between
caught and uncaught index errors were verified locally. No external packages
or input files are needed.

## Checks and current status

From this directory with the checking tools available:

```bash
python3 --version
pycodestyle --version
pycodestyle *.py
```

All 6 tracked Python files parse on local Python 3.8.20 and have the required
shebang and final newline. None has the executable Git mode; invoke them
through `python3` until that requirement is addressed.
The files pass the installed pycodestyle 2.12.1 checker.

Correction requires pycodestyle 2.7.x. Local checks are separate from a full
Ubuntu 20.04 correction run. `-B` in the examples prevents bytecode cache writes.
