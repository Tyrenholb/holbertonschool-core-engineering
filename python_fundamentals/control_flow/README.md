# Python - Control Flow

Six standalone scripts practise conditions, loops, character codes, numeric
formatting, and combinations. Two classify random integers; the others produce
fixed sequences.

## General requirements

- Correction environment: Ubuntu 20.04 LTS with Python 3.8.x.
- Every Python file must start exactly with `#!/usr/bin/env python3`.
- Python files must be executable and end with a newline.
- Code must follow PEP8, checked with pycodestyle 2.7.x.
- Output formatting must match the expected results exactly.
- External libraries are not allowed unless explicitly required by the task.

These exercises use no external runtime libraries.

## Scripts

| File | Behavior |
| --- | --- |
| [`positive_or_negative.py`](positive_or_negative.py) | Generates an integer from `-10` through `10` and prints whether it is positive, negative, or zero |
| [`last_digit.py`](last_digit.py) | Generates an integer from `-10000` through `10000`, keeps the sign of its last digit, and classifies that digit |
| [`print_alphabt.py`](print_alphabt.py) | Prints lowercase English letters except `e` and `q`, with no final output newline |
| [`print_comb2.py`](print_comb2.py) | Prints all 100 two-digit decimal values from `00` through `99`, separated by comma-space |
| [`print_comb3.py`](print_comb3.py) | Prints the 45 distinct digit pairs with the first digit smaller than the second |
| [`print_hexa.py`](print_hexa.py) | Prints decimal and hexadecimal representations of `0` through `98` |

## Usage

From the repository root:

```bash
cd python_fundamentals/control_flow
python3 -B positive_or_negative.py
python3 -B last_digit.py
python3 -B print_alphabt.py
```

The first two outputs depend on the random value. Their message forms include
`NUMBER is positive` and `Last digit of NUMBER is DIGIT and is greater than 5`.
The other branches handle zero, negative values, and remaining last digits.

The alphabet script prints:

```text
abcdfghijklmnoprstuvwxyz
```

It does not append a newline, so a shell prompt may appear immediately after
the final letter. This output behavior is separate from the requirement that
the Python source file itself ends with a newline.

Run the remaining exercises separately:

```bash
python3 -B print_comb2.py
python3 -B print_comb3.py
python3 -B print_hexa.py
```

`print_comb2.py` starts with `00, 01, 02` and ends with `99`.
`print_comb3.py` starts with `01, 02, 03` and ends with `89`; it excludes repeated
and reversed pairs. Neither prints a trailing comma-space after the final value.
Both finish with a newline.

The hexadecimal script produces 99 lines, beginning with `0 = 0x0` and ending
with `98 = 0x62`. It does not currently include `99`.

## Behavior and verification

- The scripts take no input and run their code at import time as well as when
  executed directly; they have no main guard.
- Signed last digits are calculated explicitly using `abs`, then negating for
  non-positive inputs, rather than relying on Python's negative modulo result.
- `print_comb2.py` uses a `for`/`else` to print its final value `99` separately.
- All fixed outputs were verified exactly. Random-number branches were checked
  with controlled values for positive, negative, and zero cases.
- Character output uses English-letter code points rather than locale-aware
  alphabet processing.

## Checks and current status

From this directory with the checking tools available:

```bash
python3 --version
pycodestyle --version
pycodestyle *.py
```

All 6 tracked Python files parse on local Python 3.8.20 and have the required
shebang and final newline. Their Git modes are executable.
The files pass the installed pycodestyle 2.12.1 checker.

Correction requires pycodestyle 2.7.x. Local checks are separate from a full
Ubuntu 20.04 correction run. `-B` in the examples prevents bytecode cache writes.
