# Python - Inheritance and Polymorphism

Geometry classes practise reusing validation, calling parent constructors,
overriding methods, and providing object descriptions. A separate animal
example shows the same method call producing different results for subclasses.

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
| [`base_geometry.py`](base_geometry.py) | Defines `BaseGeometry.area()`, which raises an unimplemented-operation exception, and a shared positive-integer validator |
| [`1-rectangle.py`](1-rectangle.py) | Inherits BaseGeometry and validates/stores private width and height; does not implement its own `area()` |
| [`2-rectangle.py`](2-rectangle.py) | Implements rectangle area and the string `[Rectangle] width/height` |
| [`1-square.py`](1-square.py) | Inherits the stage-2 Rectangle, validates size, initializes equal dimensions with `super`, and implements square area |
| [`2-square.py`](2-square.py) | Adds the square-specific string `[Square] size/size` |
| [`0-polymorphism_demo.py`](0-polymorphism_demo.py) | Defines Animal, Dog, and Cat, overrides `speak`, iterates mixed subclasses, and demonstrates type relationships |

The geometry hierarchy is BaseGeometry to Rectangle to Square. Each numbered
Rectangle or Square file is a separate stage, and both Square stages import
`2-rectangle.py`.

## Usage

From the repository root:

```bash
cd python_oop/inheritance
python3 -B - <<'PYTHON'
Rectangle = __import__('2-rectangle').Rectangle
Square = __import__('2-square').Square

rectangle = Rectangle(3, 4)
square = Square(3)
print(rectangle)
print(rectangle.area())
print(square)
print(square.area())
print(isinstance(square, Rectangle))
PYTHON
```

Output:

```text
[Rectangle] 3/4
12
[Square] 3/3
9
True
```

Hyphenated module names are loaded with `__import__`. Keep `base_geometry.py`
and `2-rectangle.py` alongside the dependent classes so their imports resolve.

## Polymorphism demonstration

From this directory:

```bash
python3 -B 0-polymorphism_demo.py
```

Output:

```text
Woof
Meow
Woof
Meow
Woof
True
True
True
```

The first two lines call Dog and Cat directly. The next three use the same
`speak()` expression on a mixed list. The last three confirm that a Dog is a
Dog, a Dog is an Animal, and Dog is a subclass of Animal.

## Validation and inheritance details

- `integer_validator(name, value)` requires `type(value) is int` and a value
  greater than zero. Booleans, zero, and negative dimensions are rejected.
- Errors include the supplied field name, such as `size must be an integer`
  and `size must be greater than 0`.
- Unlike the classes in `classes_and_object_model`, these geometry constructors
  require dimensions and do not allow zero.
- BaseGeometry is not an abstract class enforced by `abc`. It can be
  instantiated, but calling `area()` raises `Exception` with the message
  `area() is not implemented`. The stage-1 Rectangle inherits that behavior.
- Square uses the inherited validator and `super().__init__(size, size)`.
  Stage 1 inherits Rectangle's string format; stage 2 overrides it.
- Animal's fallback speech is `Some sound`; Dog and Cat override it. The animal
  demo has no main guard and also prints if imported.

Local checks covered the class hierarchy, inherited and overridden descriptions,
area calculations, validation types/messages, and exact demonstration output.
The current style findings are missing blank lines in the animal demo.

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
The installed pycodestyle 2.12.1 checker reports style issues in `0-polymorphism_demo.py`.

Correction requires pycodestyle 2.7.x. Local checks are separate from a full
Ubuntu 20.04 correction run. `-B` in the examples prevents bytecode cache writes.
