# Python - Core Data Structures

Eight functions practise lists, tuples, sets, dictionaries, and integer
formatting. The exercises distinguish looking up values from modifying a
container and returning the same object.

## General requirements

- Correction environment: Ubuntu 20.04 LTS with Python 3.8.x.
- Every Python file must start exactly with `#!/usr/bin/env python3`.
- Python files must be executable and end with a newline.
- Code must follow PEP8, checked with pycodestyle 2.7.x.
- Output formatting must match the expected results exactly.
- External libraries are not allowed unless explicitly required by the task.

These exercises use no external runtime libraries.

## Files and functions

| File | Behavior |
| --- | --- |
| [`element_at.py`](element_at.py) | Returns the item at a non-negative valid index, otherwise `None` |
| [`replace_in_list.py`](replace_in_list.py) | Replaces a valid indexed item in place and returns the same list; invalid indices leave it unchanged |
| [`print_list_integer.py`](print_list_integer.py) | Prints each item with integer formatting on its own line |
| [`print_matrix_integer.py`](print_matrix_integer.py) | Prints integer rows with single spaces between values |
| [`add_tuple.py`](add_tuple.py) | Adds the first two tuple positions, padding missing positions with zero and ignoring extra items |
| [`common_elements.py`](common_elements.py) | Returns the intersection of two sets |
| [`update_dictionary.py`](update_dictionary.py) | Adds or replaces a key/value in place and returns the same dictionary |
| [`best_score.py`](best_score.py) | Returns the highest-valued key, or `None` for a falsy dictionary input |
| [`test main.py`](test%20main.py) | Demonstrates `best_score` with sample scores and `None` |

## Usage

From the repository root:

```bash
cd python_fundamentals/core_data_structures
python3 -B 'test main.py'
```

Output:

```text
Molly
None
```

The caller's filename contains a space, so quote it in shell commands.
To try the reusable functions from this directory:

```bash
python3 -B - <<'PYTHON'
from add_tuple import add_tuple
from replace_in_list import replace_in_list
from common_elements import common_elements

print(add_tuple((1, 2), (3,)))
values = [1, 2, 3]
print(replace_in_list(values, 1, 9))
print(sorted(common_elements({1, 2}, {2, 3})))
PYTHON
```

Output:

```text
(4, 2)
[1, 9, 3]
[2]
```

`sorted` is used only to make the displayed set intersection deterministic.
The intersection function itself returns a set, not a list.

## Behavior and limits

- `element_at` deliberately rejects negative indices even though Python lists
  normally support them. An index beyond the end falls through to an implicit
  `None` return.
- `replace_in_list` and `update_dictionary` mutate their arguments. The tuple
  addition and set intersection return new objects.
- Score ties keep the first maximum key encountered in dictionary order.
  Values must support comparison; input types are not validated.
- Integer-printing helpers require values accepted by `{:d}` formatting.
  Matrix rows need not have equal lengths; each supplied row is printed as-is.
- `add_tuple` expects tuple inputs and addable item values. It is not a
  general arbitrary-length vector addition function.
- The functions rely on normal Python errors for unsupported types.
  The included caller executes its prints at import time.

All helper behaviors and the included caller output were checked locally,
including invalid indices, score ties, and whether mutations return the
original container.

## Checks and current status

From this directory with the checking tools available:

```bash
python3 --version
pycodestyle --version
pycodestyle *.py
```

All 9 tracked Python files parse on local Python 3.8.20 and have the required
shebang and final newline. None has the executable Git mode; invoke them
through `python3` until that requirement is addressed.
The files pass the installed pycodestyle 2.12.1 checker.

Correction requires pycodestyle 2.7.x. Local checks are separate from a full
Ubuntu 20.04 correction run. `-B` in the examples prevents bytecode cache writes.
