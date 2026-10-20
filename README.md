# Pyramids

A menu-driven Python program that prints five different kinds of pyramids. Built for the CMKL University lab combining loops, functions, `match/case` and exception handling.

## Features

| Option | Shape |
|--------|-------|
| 1 | `*` half-pyramid |
| 2 | `*` pyramid (centered) |
| 3 | `*` hollow pyramid (solid base) |
| 4 | Pyramid of numbers |
| 5 | Pyramid of letters |
| 6 | Exit |

After each shape is printed, the menu is shown again until you choose option 6.

## Requirements

- Python 3.10 or newer (the program uses `match/case`)

## Usage

```
python pyramids.py
```

Pick an option (1-6), then enter a size when prompted.

## Example output

Size 5, option 2 (pyramid):

```
    *
   ***
  *****
 *******
*********
```

Size 5, option 3 (hollow pyramid):

```
    *
   * *
  *   *
 *     *
*********
```

Size 5, option 4 (numbers):

```
    1
   123
  12345
 1234567
123456789
```

Size 5, option 5 (letters):

```
    A
   ABC
  ABCDE
 ABCDEFG
ABCDEFGHI
```

## How it works

- **One function per shape:** `half_pyramid`, `pyramid`, `hollow_pyramid`, `number_pyramid` and `letter_pyramid`, each taking `size` as a parameter.
- **Menu dispatch:** a `match/case` statement in `main()` calls the right function for the chosen option.
- **Input validation:** menu and size input are wrapped in `try/except`. Non-numeric entries are caught, and the program raises its own `ValueError` if the menu choice is outside 1-6 or the size is less than 1.
- **Letters:** the `j`-th letter in a row is `chr(ord('A') + j)`.
- **Large sizes:** for sizes above 5, digits wrap with `% 10` and letters wrap with `% 26`, so every cell stays one character wide and the shape stays aligned.
