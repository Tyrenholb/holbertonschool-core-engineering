# Python - Functions and Modules

Twelve files practise reusable functions, importing names from other modules,
and separating import behavior from direct execution. The exercises also cover
arithmetic, character handling, powers, and shared variables.

## General requirements

- Correction environment: Ubuntu 20.04 LTS with Python 3.8.x.
- Every Python file must start exactly with `#!/usr/bin/env python3`.
- Python files must be executable and end with a newline.
- Code must follow PEP8, checked with pycodestyle 2.7.x.
- Output formatting must match the expected results exactly.
- External libraries are not allowed unless explicitly required by the task.

These exercises use no external runtime libraries.

## Files

| File | Behavior |
| --- | --- |
| [`add_0.py`](add_0.py) | Defines `add(a, b)` |
| [`add.py`](add.py) | Imports `add` from `add_0` and prints `1 + 2 = 3` when run directly |
| [`simple_add.py`](simple_add.py) | Defines another addition function; its guarded demo prints `8` |
| [`test_import.py`](test_import.py) | Imports `simple_add` without triggering its guarded print |
| [`calculator_1.py`](calculator_1.py) | Defines addition, subtraction, multiplication, and true division |
| [`calculation.py`](calculation.py) | Imports the calculator functions and demonstrates them with `10` and `5` |
| [`islower.py`](islower.py) | Checks whether a single character's code is in the lowercase English-letter range |
| [`uppercase.py`](uppercase.py) | Prints a string with lowercase English letters converted to uppercase |
| [`print_last_digit.py`](print_last_digit.py) | Prints and returns the non-negative last decimal digit, without adding a newline |
| [`pow.py`](pow.py) | Computes integer-exponent powers using repeated multiplication and reciprocals for negative exponents |
| [`variable_load_5.py`](variable_load_5.py) | Defines the module variable `a = 98` |
| [`variable_load.py`](variable_load.py) | Imports `a` and prints it when run directly |

## Usage

From the repository root:

```bash
cd python_fundamentals/functions_modules
python3 -B add.py
python3 -B calculation.py
python3 -B variable_load.py
```

Combined output, in that order:

```text
1 + 2 = 3
10 + 5 = 15
10 - 5 = 5
10 * 5 = 50
10 / 5 = 2.0
98
```

Run the import demonstration separately:

```bash
python3 -B simple_add.py
python3 -B test_import.py
```

The first command prints `8`. The second prints nothing because the imported
module's demonstration is protected by `if __name__ == "__main__"`.

To call individual helpers from this directory:

```bash
python3 -B - <<'PYTHON'
from pow import pow
from islower import islower
from uppercase import uppercase

print(pow(2, -3))
print(islower("a"))
uppercase("Hello!")
PYTHON
```

Output:

```text
0.125
True
HELLO!
```

## Behavior and limits

- Keep the related files together so their local imports resolve. The reusable
  function modules do not print merely because they are imported.
- `calculator_1.div` uses `/`, not integer floor division. Division by zero is
  not caught.
- `pow` expects an integer exponent for `range(abs(b))`; its work grows with
  the exponent's absolute value. A zero base with a negative exponent raises
  division by zero. Exponent zero returns `1`, including `pow(0, 0)`.
- Character helpers use ASCII-compatible English-letter code points, not full
  Unicode case conversion. `islower` requires exactly one character for `ord`.
- `print_last_digit(-123)` prints `3` without a newline and returns `3`.
  Its caller decides whether to print the returned value or an extra newline.
- These small helpers rely on Python's normal errors for unsupported inputs.
  They do not provide a validated interactive calculator.

All included callers and the examples above were verified locally, including
silent import behavior, floating-point division, and negative exponents.

## Checks and current status

From this directory with the checking tools available:

```bash
python3 --version
pycodestyle --version
pycodestyle *.py
```

All 12 tracked Python files parse on local Python 3.8.20 and have the required
shebang and final newline. 11 lack the executable Git mode.
The installed pycodestyle 2.12.1 checker reports style issues in `simple_add.py`.

Correction requires pycodestyle 2.7.x. Local checks are separate from a full
Ubuntu 20.04 correction run. `-B` in the examples prevents bytecode cache writes.
