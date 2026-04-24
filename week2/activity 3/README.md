# Calculator Program

This project contains a Python calculator that uses **object-oriented design** and is split across two modules:

| File | Role |
|------|------|
| `calculator_class.py` | `Calculator` class only (operation logic). |
| `calculator.py` | `parse_value`, `main`, and the `if __name__ == "__main__"` entry point. |

## Design

- **`Calculator`** (`calculator_class.py`) — encapsulates supported math operations.
  - `ensure_binary_operator(operator_symbol)` — validates `+`, `-`, `*`, `/`, `%`.
  - `apply_binary(left, operator_symbol, right)` — performs a binary operation.
  - `factorial(value)` — factorial for non-negative integers.
- **`parse_value(raw)`** (`calculator.py`) — parses Python-style literals (with complex fallback).
- **`main()`** (`calculator.py`) — interactive loop: creates a `Calculator`, reads input, prints the result.

## Supported operations

- Addition: `+`
- Subtraction: `-`
- Multiplication: `*`
- Division: `/`
- Modulo: `%`
- Factorial: `factorial`

It accepts Python-style values such as:

- Integers: `5`
- Floats: `3.14`
- Complex numbers: `2+3j`
- Strings: `"hello"`
- Lists: `[1, 2]`

## Requirements

- Python 3

## How to run

From this folder, run:

```bash
python3 calculator.py
```

## Example

```text
Basic Mathematical Operations
Supported operators: +, -, *, /, %, factorial
Enter an operator: +
Enter the first value: 2+3j
Enter the second value: 4-1j
Result: (6+2j)
```

## Factorial example

```text
Enter an operator: factorial
Enter a non-negative integer: 5
Result: 120
```
