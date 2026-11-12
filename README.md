# Python - Core Engineering

This repository contains my Holberton School exercises in Python fundamentals,
file handling, and object-oriented programming. The projects move from fixed
output and control flow to reusable functions, collections, exceptions, classes,
and inheritance.

There are 54 Python source files across eight exercise folders. Each folder's
README explains its functions or scripts, examples, and current limitations.

## Project groups

| Group | What it covers |
| --- | --- |
| [`python_advanced`](python_advanced/) | Reading, overwriting, and appending UTF-8 text files |
| [`python_fundamentals`](python_fundamentals/) | Conditions, loops, collections, exceptions, functions, imports, and formatted output |
| [`python_oop`](python_oop/) | Progressive class implementations, properties, validation, inheritance, and polymorphism |

## Exercise folders

| Folder | Python files | What it covers |
| --- | --- | --- |
| [`python_advanced/file_handling`](python_advanced/file_handling/README.md) | 4 | File modes, context managers, character counts, and preserving output newlines |
| [`python_fundamentals/control_flow`](python_fundamentals/control_flow/README.md) | 6 | Random-number classification, character ranges, digit combinations, and hexadecimal output |
| [`python_fundamentals/core_data_structures`](python_fundamentals/core_data_structures/README.md) | 9 | Lists, tuples, sets, dictionaries, in-place changes, lookups, and integer formatting |
| [`python_fundamentals/exception_handling`](python_fundamentals/exception_handling/README.md) | 6 | Specific exception handlers, safe printing, division, `finally`, and explicit raises |
| [`python_fundamentals/functions_modules`](python_fundamentals/functions_modules/README.md) | 12 | Functions, local imports, shared variables, main guards, arithmetic, and character helpers |
| [`python_fundamentals/hello_world`](python_fundamentals/hello_world/README.md) | 1 | Fixed labels, f-strings, floating-point formatting, and Boolean output |
| [`python_oop/classes_and_object_model`](python_oop/classes_and_object_model/README.md) | 10 | Independent Square/Rectangle stages, private attributes, properties, areas, perimeters, and text rendering |
| [`python_oop/inheritance`](python_oop/inheritance/README.md) | 6 | Shared geometry validation, parent constructors, method overrides, type relationships, and animal polymorphism |

Counts include demonstration callers as well as reusable implementations.

## General requirements

- Corrections run on Ubuntu 20.04 LTS with Python 3.8.x.
- Every Python file must start exactly with:

```python
#!/usr/bin/env python3
```

- Python files must be executable and end with a newline.
- Code must follow PEP8, checked with pycodestyle 2.7.x.
- Output must match expected formatting exactly.
- External libraries are not allowed unless explicitly requested by the task.

The checked-in exercises use built-ins and the standard library; no external
runtime package installation is needed. These requirements describe the
submission standard, not a claim that every file currently meets it.

## Run an exercise

There is no single application entry point. Some scripts run immediately;
others define functions or classes for a caller.

For a standalone example, from the repository root:

```bash
python3 -B python_fundamentals/hello_world/structured_output.py
```

Output:

```text
Language: Python
Version: 3
Pi approx: 3.14
Computation valid: True
```

For a caller that imports nearby modules:

```bash
cd python_fundamentals/functions_modules
python3 -B calculation.py
```

Output:

```text
10 + 5 = 15
10 - 5 = 5
10 * 5 = 50
10 / 5 = 2.0
```

Run other examples using their folder README. Keep related modules together
for local imports. Some filenames contain hyphens and are loaded through
`__import__`; the data-structures caller named `test main.py` needs shell quoting.

`-B` prevents bytecode cache writes. It does not suppress output or file changes.

## Check the requirements

Confirm the interpreter and style-checker versions in your chosen environment:

```bash
python3 --version
pycodestyle --version
```

Use Python 3.8.x and pycodestyle 2.7.x for the correction toolchain. Run the
style checker on the selected project, for example:

```bash
pycodestyle python_fundamentals/control_flow/*.py
```

Check the first line, final newline, and executable file mode separately from
style. A Python file can run through `python3` without an executable bit;
that alone does not establish direct-execution compliance.

## Current verification

- All 54 tracked Python sources parse on local Python 3.8.20, start with the
  required shebang, and end with a newline.
- Eight files have executable Git modes; 46 do not. Each folder README records
  its status. This documentation update does not change source permissions.
- The installed checker is pycodestyle 2.12.1, rather than the required 2.7.x.
  It reports style issues in file handling, functions/modules, class stages,
  and the inheritance demonstration. The other four folders pass that checker.
- Fixed output, selected function behaviors, exception paths, validation
  messages, class stages, and import behavior were checked locally. Random
  branches were tested with controlled values, and file operations used
  temporary storage.

These checks are separate from a full Ubuntu 20.04 correction run and do not
replace the task-specific expected outputs.

## Behavior to keep in mind

- Output formatting is part of the exercises: some helpers deliberately omit
  a newline or separators, and floating-point division prints values such as
  `2.0` rather than `2`.
- File writers can create or replace files, while append operations add content
  on every call. The file-handling driver appends even if imported.
- Main guards are present in some callers, not all. Check a module before
  importing it if its top-level code prints or changes files.
- Numbered OOP files are separate implementation stages. Earlier classes may
  lack methods available later, and validation rules differ between projects:
  the basic geometry classes allow zero dimensions, while inheritance tasks
  require dimensions greater than zero.
- Error-handling exercises catch specific exceptions. A function named safe
  does not necessarily handle every invalid input.
