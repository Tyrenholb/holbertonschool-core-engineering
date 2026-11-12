# Python - File Handling

Three functions practise reading, overwriting, and appending UTF-8 text files.
They use `with` blocks to close files automatically and return character counts
where text is written.

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
| [`read_file.py`](read_file.py) | `read_file(filename="")` prints the entire file without adding an extra newline; returns `None` |
| [`write_file.py`](write_file.py) | `write_file(filename="", text="")` creates or overwrites a file and returns the number of characters written |
| [`append_write.py`](append_write.py) | `append_write(filename="", text="")` creates or appends to a file and returns the number of characters added |
| [`main.py`](main.py) | Appends `This School is so cool!` plus a newline to `file_append.txt`, then prints the count `23` |

## Usage

From the repository root:

```bash
cd python_advanced/file_handling
python3 -B - <<'PYTHON'
from write_file import write_file
from append_write import append_write
from read_file import read_file

print(write_file("sample.txt", "Hello\n"))
print(append_write("sample.txt", "Python\n"))
read_file("sample.txt")
PYTHON
```

Output:

```text
6
7
Hello
Python
```

Run the included append demonstration separately:

```bash
python3 -B main.py
```

It prints `23` on each successful run. Each run appends another line rather
than replacing the previous content.

## Behavior and limits

- `write_file` and `append_write` return counts, not file contents, despite
  wording in their current docstrings. They do not print the written text.
- Counts are Unicode characters, not UTF-8 byte counts. A newline counts as
  one character in the supplied strings.
- Relative filenames are resolved from the current working directory. The
  empty-string filename defaults do not identify a usable file.
- File/permission and decoding errors are not caught. Missing parent directories
  are not created, and `read_file` reads the whole file into memory.
- `main.py` has no main guard. Importing it also appends to its fixed file and
  prints the count; import the helper modules instead for reusable functions.

The example and driver output were verified on temporary files, preserving
the repository. Remove only generated samples when finished:

```bash
rm -f sample.txt file_append.txt
```

## Checks and current status

From this directory with the checking tools available:

```bash
python3 --version
pycodestyle --version
pycodestyle *.py
```

All 4 tracked Python files parse on local Python 3.8.20 and have the required
shebang and final newline. None has the executable Git mode; invoke them
through `python3` until that requirement is addressed.
The installed pycodestyle 2.12.1 checker reports style issues in `main.py`.

Correction requires pycodestyle 2.7.x. Local checks are separate from a full
Ubuntu 20.04 correction run. `-B` in the examples prevents bytecode cache writes.
