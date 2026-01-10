"""
Unit tests for the calculator core functionality.
"""

import pytest
import math
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

    def test_add_invalid_input_type(self):
        """Test addition with invalid input types."""
        with pytest.raises(TypeError, match=r"Expected int or float, got str"):
            self.calc.add("invalid", 5)
        with pytest.raises(TypeError, match=r"Expected int or float, got str"):
            self.calc.add(5, "invalid")

    def test_subtract_invalid_input_type(self):
        """Test subtraction with invalid input types."""
        with pytest.raises(TypeError, match=r"Expected int or float, got str"):
            self.calc.subtract("invalid", 5)
        with pytest.raises(TypeError, match=r"Expected int or float, got str"):
            self.calc.subtract(5, "invalid")

    def test_multiply_invalid_input_type(self):
        """Test multiplication with invalid input types."""
        with pytest.raises(TypeError, match=r"Expected int or float, got str"):
            self.calc.multiply("invalid", 5)
        with pytest.raises(TypeError, match=r"Expected int or float, got str"):
            self.calc.multiply(5, "invalid")

    def test_divide_invalid_input_type(self):
        """Test division with invalid input types."""
        with pytest.raises(TypeError, match=r"Expected int or float, got str"):
            self.calc.divide("invalid", 5)
        with pytest.raises(TypeError, match=r"Expected int or float, got str"):
            self.calc.divide(5, "invalid")

    def test_operations_with_nan_values(self):
        """Test operations with NaN values."""
        nan_value = float('nan')
        with pytest.raises(ValueError, match=r"Value must be a finite number, got nan"):
            self.calc.add(nan_value, 5)
        with pytest.raises(ValueError, match=r"Value must be a finite number, got nan"):
            self.calc.add(5, nan_value)

    def test_operations_with_infinite_values(self):
        """Test operations with infinite values."""
        inf_value = float('inf')
        with pytest.raises(ValueError, match=r"Value must be a finite number, got inf"):
            self.calc.multiply(inf_value, 5)
        with pytest.raises(ValueError, match=r"Value must be a finite number, got inf"):
            self.calc.multiply(5, -inf_value)

    def test_decimal_precision_addition(self):
        """Test addition with decimal precision."""
        result = self.calc.add(0.1, 0.2)
        assert result == pytest.approx(0.3)

    def test_decimal_precision_subtraction(self):
        """Test subtraction with decimal precision."""
        result = self.calc.subtract(1.0, 0.9)
        assert result == pytest.approx(0.1)

    def test_decimal_precision_multiplication(self):
        """Test multiplication with decimal precision."""
        result = self.calc.multiply(0.1, 3)
        assert result == pytest.approx(0.3)

    def test_decimal_precision_division(self):
        """Test division with decimal precision."""
        result = self.calc.divide(1, 3)
        assert result == pytest.approx(0.3333333333333333)

    def test_decimal_precision_complex_operations(self):
        """Test complex operations with decimal precision."""
        result = self.calc.multiply(self.calc.add(0.1, 0.2), 10)
        assert result == pytest.approx(3.0)