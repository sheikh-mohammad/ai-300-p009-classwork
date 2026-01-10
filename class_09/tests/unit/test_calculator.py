"""
Unit tests for the calculator core functionality.
"""

import pytest
from src.calculator.core import Calculator


class TestCalculator:
    """Test cases for the Calculator class."""

    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.calc = Calculator()

    def test_add_positive_numbers(self):
        """Test addition of positive numbers."""
        assert self.calc.add(2, 3) == 5
        assert self.calc.add(10, 5) == 15

    def test_add_negative_numbers(self):
        """Test addition of negative numbers."""
        assert self.calc.add(-2, -3) == -5
        assert self.calc.add(-10, 5) == -5

    def test_add_zero(self):
        """Test addition involving zero."""
        assert self.calc.add(5, 0) == 5
        assert self.calc.add(0, 5) == 5
        assert self.calc.add(0, 0) == 0

    def test_subtract_positive_numbers(self):
        """Test subtraction of positive numbers."""
        assert self.calc.subtract(5, 3) == 2
        assert self.calc.subtract(10, 5) == 5

    def test_subtract_negative_results(self):
        """Test subtraction resulting in negative numbers."""
        assert self.calc.subtract(3, 5) == -2
        assert self.calc.subtract(-5, 3) == -8

    def test_subtract_zero(self):
        """Test subtraction involving zero."""
        assert self.calc.subtract(5, 0) == 5
        assert self.calc.subtract(0, 5) == -5
        assert self.calc.subtract(0, 0) == 0

    def test_multiply_positive_numbers(self):
        """Test multiplication of positive numbers."""
        assert self.calc.multiply(3, 4) == 12
        assert self.calc.multiply(10, 5) == 50

    def test_multiply_by_zero(self):
        """Test multiplication by zero."""
        assert self.calc.multiply(5, 0) == 0
        assert self.calc.multiply(0, 5) == 0
        assert self.calc.multiply(0, 0) == 0

    def test_multiply_negative_numbers(self):
        """Test multiplication involving negative numbers."""
        assert self.calc.multiply(-3, 4) == -12
        assert self.calc.multiply(3, -4) == -12
        assert self.calc.multiply(-3, -4) == 12

    def test_divide_positive_numbers(self):
        """Test division of positive numbers."""
        assert self.calc.divide(10, 2) == 5
        assert self.calc.divide(15, 3) == 5

    def test_divide_fractional_results(self):
        """Test division resulting in fractional numbers."""
        assert self.calc.divide(7, 2) == 3.5
        assert self.calc.divide(1, 3) == pytest.approx(0.3333333333333333)

    def test_divide_negative_numbers(self):
        """Test division involving negative numbers."""
        assert self.calc.divide(-10, 2) == -5
        assert self.calc.divide(10, -2) == -5
        assert self.calc.divide(-10, -2) == 5

    def test_divide_by_zero_raises_exception(self):
        """Test that division by zero raises ZeroDivisionError."""
        with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
            self.calc.divide(10, 0)

    def test_divide_zero_by_number(self):
        """Test dividing zero by a number."""
        assert self.calc.divide(0, 5) == 0
        assert self.calc.divide(0, -5) == 0