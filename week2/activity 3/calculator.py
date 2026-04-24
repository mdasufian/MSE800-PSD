import ast

from calculator_class import Calculator


def parse_value(raw):
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


def main():
    calc = Calculator()
    print("Basic Mathematical Operations")
    print("Supported operators: +, -, *, /, %, factorial")

    operation = input("Enter an operator: ").strip().lower()

    try:
        if operation == "factorial":
            value = parse_value(input("Enter a non-negative integer: "))
            result = calc.factorial(value)
        else:
            left = parse_value(input("Enter the first value: "))
            right = parse_value(input("Enter the second value: "))
            result = calc.apply_binary(left, operation, right)

        print(f"Result: {result}")
    except Exception as exc:
        print(f"Error: {exc}")


if __name__ == "__main__":
    main()
