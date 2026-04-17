from __future__ import annotations

import ast
import math


def parse_value(raw: str):
    """Parse a Python-style literal, falling back to complex parsing."""
    text = raw.strip()

    try:
        return ast.literal_eval(text)
    except (ValueError, SyntaxError):
        try:
            return complex(text)
        except ValueError as exc:
            raise ValueError(
                f"Could not parse {raw!r}. Use a valid Python-style value."
            ) from exc


def apply_basic_operation(left, operator_symbol: str, right):
    """Apply a supported binary operation."""
    if operator_symbol == "+":
        return left + right
    if operator_symbol == "-":
        return left - right
    if operator_symbol == "*":
        return left * right
    if operator_symbol == "/":
        return left / right
    if operator_symbol == "%":
        return left % right

    raise ValueError(f"Unsupported operator: {operator_symbol}")


def calculate_factorial(value: int) -> int:
    """Calculate factorial for a non-negative integer."""
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError("Factorial only works with non-negative integers.")
    if value < 0:
        raise ValueError("Factorial is not defined for negative integers.")

    return math.factorial(value)


def main() -> None:
    print("Basic Mathematical Operations")
    print("Supported operators: +, -, *, /, %, factorial")

    operation = input("Enter an operator: ").strip().lower()

    try:
        if operation == "factorial":
            value = parse_value(input("Enter a non-negative integer: "))
            result = calculate_factorial(value)
        else:
            left = parse_value(input("Enter the first value: "))
            right = parse_value(input("Enter the second value: "))
            result = apply_basic_operation(left, operation, right)

        print(f"Result: {result}")
    except Exception as exc:
        print(f"Error: {exc}")


if __name__ == "__main__":
    main()
