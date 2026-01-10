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

    def test_cli_invalid_number_error(self):
        """Test CLI invalid number error handling."""
        with patch('sys.argv', ['calc', 'abc', '+', '3']):
            with patch('sys.stdout', new_callable=StringIO):
                with patch('sys.stderr', new_callable=StringIO):
                    with pytest.raises(SystemExit) as exc_info:
                        main()
                    assert exc_info.value.code == 1

    def test_cli_invalid_operator_error(self):
        """Test CLI invalid operator error handling."""
        # argparse will catch invalid operators at parse time
        import subprocess
        result = subprocess.run([sys.executable, '-c',
                                 'import sys; sys.argv = ["calc", "5", "%", "3"]; '
                                 'from src.calculator.cli import main; main()'],
                                capture_output=True, text=True)
        assert result.returncode != 0
        assert "invalid choice" in result.stderr.lower()

    def test_cli_nan_input_error(self):
        """Test CLI with NaN input."""
        with patch('sys.argv', ['calc', 'nan', '+', '3']):
            with patch('sys.stdout', new_callable=StringIO):
                with patch('sys.stderr', new_callable=StringIO):
                    with pytest.raises(SystemExit) as exc_info:
                        main()
                    assert exc_info.value.code == 1

    def test_cli_infinity_input_error(self):
        """Test CLI with infinity input."""
        with patch('sys.argv', ['calc', 'inf', '+', '3']):
            with patch('sys.stdout', new_callable=StringIO):
                with patch('sys.stderr', new_callable=StringIO):
                    with pytest.raises(SystemExit) as exc_info:
                        main()
                    assert exc_info.value.code == 1

    @patch('sys.argv', ['calc', '0.1', '+', '0.2'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_cli_decimal_addition(self, mock_stdout):
        """Test CLI decimal addition operation."""
        main()
        output = mock_stdout.getvalue().strip()
        # The result should be approximately 0.3, considering float precision
        assert float(output) == pytest.approx(0.3)

    @patch('sys.argv', ['calc', '1.5', '*', '2.5'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_cli_decimal_multiplication(self, mock_stdout):
        """Test CLI decimal multiplication operation."""
        main()
        output = mock_stdout.getvalue().strip()
        assert float(output) == pytest.approx(3.75)

    @patch('sys.argv', ['calc', '7.0', '/', '3.0'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_cli_decimal_division(self, mock_stdout):
        """Test CLI decimal division operation."""
        main()
        output = mock_stdout.getvalue().strip()
        assert float(output) == pytest.approx(2.3333333333333333)