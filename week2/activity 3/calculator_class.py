import math


class Calculator:
    """Encapsulates supported mathematical operations."""

    _BINARY_OPS = frozenset({"+", "-", "*", "/", "%"})

    def ensure_binary_operator(self, operator_symbol):
        if operator_symbol not in self._BINARY_OPS:
            raise ValueError(f"Unsupported operator: {operator_symbol}")

    def apply_binary(self, left, operator_symbol, right):
        self.ensure_binary_operator(operator_symbol)
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

    def factorial(self, value):
        if isinstance(value, bool) or not isinstance(value, int):
            raise TypeError("Factorial only works with non-negative integers.")
        if value < 0:
            raise ValueError("Factorial is not defined for negative integers.")
        return math.factorial(value)
