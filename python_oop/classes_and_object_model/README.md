# Python - Classes and the Object Model

Progressive Square and Rectangle implementations practise classes, constructors,
private attributes, properties, validation, and printable object behavior.
Each numbered file defines an independent version of its class; the Square
stages do not inherit from one another.

## General requirements

- Correction environment: Ubuntu 20.04 LTS with Python 3.8.x.
- Every Python file must start exactly with `#!/usr/bin/env python3`.
- Python files must be executable and end with a newline.
- Code must follow PEP8, checked with pycodestyle 2.7.x.
- Output formatting must match the expected results exactly.
- External libraries are not allowed unless explicitly required by the task.

These exercises use no external runtime libraries.

## Square progression

| File | What it adds |
| --- | --- |
| [`0-square.py`](0-square.py) | An empty `Square` class |
| [`1-square.py`](1-square.py) | A required size stored in a private attribute, without validation |
| [`2-square.py`](2-square.py) | Default size `0`, exact integer-type validation, and rejection of negative sizes |
| [`3-square.py`](3-square.py) | `area()` using the private size |
| [`4-square.py`](4-square.py) | A validated `size` property that also handles later assignments |
| [`5-square.py`](5-square.py) | `my_print()` to draw the square with `#` characters |
| [`6-square.py`](6-square.py) | A validated `(x, y)` position, offset string representation, and printing through `__str__` |

## Rectangle files

| File | What it does |
| --- | --- |
| [`1-rectangle.py`](1-rectangle.py) | Stores width and height through validated properties, defaulting both to zero |
| [`2-rectangle.py`](2-rectangle.py) | Adds `area()` and `perimeter()`; perimeter is zero when either dimension is zero |
| [`testmain.py`](testmain.py) | Prints area/perimeter before and after changing a rectangle's dimensions |

## Usage

Numbered filenames contain hyphens, so the examples load them with `__import__`
rather than normal `from` syntax. From the repository root:

```bash
cd python_oop/classes_and_object_model
python3 -B - <<'PYTHON'
Square = __import__('6-square').Square
Rectangle = __import__('2-rectangle').Rectangle

rectangle = Rectangle(2, 4)
print("Area: {} - Perimeter: {}".format(
    rectangle.area(), rectangle.perimeter()
))
Square(2).my_print()
PYTHON
```

Output:

```text
Area: 8 - Perimeter: 12
##
##
```

The included rectangle caller can also be run directly:

```bash
python3 -B testmain.py
```

It reports area `8` and perimeter `12` for dimensions `2` by `4`, prints a
separator, then reports area `30` and perimeter `26` after changing the
rectangle to `10` by `3`.

## Validation and object behavior

- Square stage 2 onward requires `type(size) is int` and `size >= 0`.
  Later size properties enforce the same rules. Boolean values are rejected.
- Rectangle dimensions also require exact integers and allow zero. Errors
  name the relevant dimension, such as `width must be an integer` or
  `height must be >= 0`.
- Double-underscore attributes use Python name mangling; they are not a
  security boundary. Properties provide the intended validated access path.
- Stage 6 requires an exact two-item tuple of non-negative exact integers.
  Despite the error message mentioning positive integers, zero offsets are valid.
- Position `(x, y)` adds `y` leading newlines and `x` spaces before every row.
  A zero-size square's string is empty and `my_print()` prints one newline.
- `__str__` returns text; `my_print` writes it. Earlier versions do not all
  provide these methods or public size properties.
- The classes do not implement equality comparisons or automatic geometry
  relationships. Rectangle and Square here are separate exercises.

All class stages were checked locally, including validation messages, property
updates, offset rendering, zero-dimension metrics, and the included caller.
The style findings in `1-square.py` concern spacing/comments; `testmain.py`
also contains lines longer than the style limit.

## Checks and current status

From this directory with the checking tools available:

```bash
python3 --version
pycodestyle --version
pycodestyle *.py
```

All 10 tracked Python files parse on local Python 3.8.20 and have the required
shebang and final newline. None has the executable Git mode; invoke them
through `python3` until that requirement is addressed.
The installed pycodestyle 2.12.1 checker reports style issues in `1-square.py`, `testmain.py`.

Correction requires pycodestyle 2.7.x. Local checks are separate from a full
Ubuntu 20.04 correction run. `-B` in the examples prevents bytecode cache writes.
