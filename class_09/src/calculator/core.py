"""
Core calculator functionality for basic arithmetic operations.
"""

from typing import Union


class Calculator:
    """
    A calculator class that performs basic arithmetic operations.
    """

    @staticmethod
    def _validate_number(value: Union[int, float]) -> Union[int, float]:
        """
        Validate that the input is a valid number.

        Args:
            value: The value to validate

        Returns:
            The validated number

        Raises:
            TypeError: If the value is not a number
            ValueError: If the value is NaN or infinite
        """
        if not isinstance(value, (int, float)):
            raise TypeError(f"Expected int or float, got {type(value).__name__}")

        if isinstance(value, float):
            import math
            if math.isnan(value) or math.isinf(value):
                raise ValueError(f"Value must be a finite number, got {value}")

        return value

    def add(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """
        Add two numbers.

        Args:
            a: First number
            b: Second number

        Returns:
            The sum of a and b

        Raises:
            TypeError: If inputs are not numbers
            ValueError: If inputs are NaN or infinite
        """
        a = self._validate_number(a)
        b = self._validate_number(b)
        return a + b

    def subtract(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """
        Subtract second number from first number.

        Args:
            a: First number
            b: Second number

        Returns:
            The difference of a and b

        Raises:
            TypeError: If inputs are not numbers
            ValueError: If inputs are NaN or infinite
        """
        a = self._validate_number(a)
        b = self._validate_number(b)
        return a - b

    def multiply(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """
        Multiply two numbers.

        Args:
            a: First number
            b: Second number

        Returns:
            The product of a and b

        Raises:
            TypeError: If inputs are not numbers
            ValueError: If inputs are NaN or infinite
        """
        a = self._validate_number(a)
        b = self._validate_number(b)
        return a * b

    def divide(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """
        Divide first number by second number.

        Args:
            a: First number (dividend)
            b: Second number (divisor)

        Returns:
            The quotient of a divided by b

        Raises:
            TypeError: If inputs are not numbers
            ValueError: If inputs are NaN or infinite
            ZeroDivisionError: If b is zero
        """
        a = self._validate_number(a)
        b = self._validate_number(b)
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b