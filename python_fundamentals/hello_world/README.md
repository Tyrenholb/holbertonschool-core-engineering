# Python - Hello World and Structured Output

A short script introduces variables, expressions, f-strings, and predictable
terminal output. It combines fixed labels with a rounded number and a Boolean
result.

## General requirements

- Correction environment: Ubuntu 20.04 LTS with Python 3.8.x.
- Every Python file must start exactly with `#!/usr/bin/env python3`.
- Python files must be executable and end with a newline.
- Code must follow PEP8, checked with pycodestyle 2.7.x.
- Output formatting must match the expected results exactly.
- External libraries are not allowed unless explicitly required by the task.

These exercises use no external runtime libraries.

## File

[`structured_output.py`](structured_output.py) sets `pi` to `3.14159`, evaluates
whether `2 + 2 == 4`, and prints four labeled lines.

| Output line | What it demonstrates |
| --- | --- |
| `Language: Python` | Fixed text |
| `Version: 3` | A fixed version label, not a runtime interpreter check |
| `Pi approx: 3.14` | Floating-point formatting with two decimal places |
| `Computation valid: True` | Formatting the result of a Boolean expression |

## Usage

From the repository root:

```bash
cd python_fundamentals/hello_world
python3 -B structured_output.py
```

Output:

```text
Language: Python
Version: 3
Pi approx: 3.14
Computation valid: True
```

The exact four-line output was verified locally, including spaces,
capitalization, and the final newline.

## Behavior

- There are no command-line arguments, input files, or user prompts.
- Formatting `pi` with `.2f` changes its displayed representation, not the
  stored variable's value.
- Python displays this Boolean as `True`, with a capital `T`.
- The script has no main guard, so importing it also prints the four lines.
- The `Version: 3` text is hard-coded. Use `python3 --version` to check the
  actual interpreter separately.

## Checks and current status

From this directory with the checking tools available:

```bash
python3 --version
pycodestyle --version
pycodestyle *.py
```

All 1 tracked Python files parse on local Python 3.8.20 and have the required
shebang and final newline. Their Git modes are executable.
The files pass the installed pycodestyle 2.12.1 checker.

Correction requires pycodestyle 2.7.x. Local checks are separate from a full
Ubuntu 20.04 correction run. `-B` in the examples prevents bytecode cache writes.
