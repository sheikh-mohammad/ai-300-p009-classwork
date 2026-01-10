"""
Core calculator functionality for basic arithmetic operations.
"""

from typing import Union


class Calculator:
    """
    A calculator class that performs basic arithmetic operations.
    """

    def add(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """
        Add two numbers.

        Args:
            a: First number
            b: Second number

        Returns:
            The sum of a and b
        """
        return a + b

    def subtract(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """
        Subtract second number from first number.

        Args:
            a: First number
            b: Second number

        Returns:
            The difference of a and b
        """
        return a - b

    def multiply(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """
        Multiply two numbers.

        Args:
            a: First number
            b: Second number

        Returns:
            The product of a and b
        """
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
            ZeroDivisionError: If b is zero
        """
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b