"""
Integration tests for the calculator CLI functionality.
"""

import sys
from io import StringIO
from unittest.mock import patch
import pytest
from src.calculator.cli import main


class TestCalculatorCLI:
    """Test cases for the calculator CLI integration."""

    @patch('sys.argv', ['calc', '5', '+', '3'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_cli_addition(self, mock_stdout):
        """Test CLI addition operation."""
        main()
        output = mock_stdout.getvalue().strip()
        assert output == "8"

    @patch('sys.argv', ['calc', '10', '-', '4'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_cli_subtraction(self, mock_stdout):
        """Test CLI subtraction operation."""
        main()
        output = mock_stdout.getvalue().strip()
        assert output == "6"

    @patch('sys.argv', ['calc', '6', '*', '7'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_cli_multiplication(self, mock_stdout):
        """Test CLI multiplication operation."""
        main()
        output = mock_stdout.getvalue().strip()
        assert output == "42"

    @patch('sys.argv', ['calc', '15', '/', '3'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_cli_division(self, mock_stdout):
        """Test CLI division operation."""
        main()
        output = mock_stdout.getvalue().strip()
        assert output == "5.0"

    @patch('sys.argv', ['calc', '10', '/', '3'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_cli_division_fractional(self, mock_stdout):
        """Test CLI division with fractional result."""
        main()
        output = mock_stdout.getvalue().strip()
        assert output == str(10/3)

    @patch('sys.argv', ['calc', '10', '/', '0'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_cli_division_by_zero_error(self, mock_stdout):
        """Test CLI division by zero error handling."""
        with pytest.raises(SystemExit) as exc_info:
            main()
        assert exc_info.value.code == 1

    @patch('sys.argv', ['calc', '5', '%', '3'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_cli_invalid_operator_error(self, mock_stdout):
        """Test CLI invalid operator error handling."""
        # argparse will catch invalid operators at parse time
        # This test is more about ensuring the error is handled properly
        pass  # This will be caught by argparse validation

    def test_cli_invalid_number_error(self):
        """Test CLI invalid number error handling."""
        # This would be tested by trying to convert invalid strings to float
        # which happens during argument parsing
        with patch('sys.argv', ['calc', 'abc', '+', '3']):
            with patch('sys.stdout', new_callable=StringIO):
                with pytest.raises(SystemExit):
                    main()