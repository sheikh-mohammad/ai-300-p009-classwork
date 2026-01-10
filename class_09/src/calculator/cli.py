"""
Command-line interface for the calculator.
"""

import sys
import argparse
import math
from typing import Union

from .core import Calculator


def parse_arguments() -> argparse.Namespace:
    """
    Parse command line arguments.

    Returns:
        Parsed arguments namespace
    """
    parser = argparse.ArgumentParser(description="A command-line calculator")
    parser.add_argument("first_number", type=float, help="The first number")
    parser.add_argument("operator", choices=["+", "-", "*", "/"], help="The operator (+, -, *, /)")
    parser.add_argument("second_number", type=float, help="The second number")

    return parser.parse_args()


def format_result(result: Union[int, float]) -> str:
    """
    Format the result appropriately (remove decimal if it's a whole number).

    Args:
        result: The calculation result

    Returns:
        Formatted result string
    """
    if isinstance(result, float) and result.is_integer():
        return str(int(result))
    return str(result)


def main() -> None:
    """
    Main entry point for the calculator CLI.
    """
    try:
        args = parse_arguments()

        # Additional validation for NaN and infinity
        if math.isnan(args.first_number) or math.isinf(args.first_number):
            print(f"Error: Invalid input - first number must be a finite number", file=sys.stderr)
            sys.exit(1)

        if math.isnan(args.second_number) or math.isinf(args.second_number):
            print(f"Error: Invalid input - second number must be a finite number", file=sys.stderr)
            sys.exit(1)

        calc = Calculator()

        if args.operator == "+":
            result = calc.add(args.first_number, args.second_number)
        elif args.operator == "-":
            result = calc.subtract(args.first_number, args.second_number)
        elif args.operator == "*":
            result = calc.multiply(args.first_number, args.second_number)
        elif args.operator == "/":
            result = calc.divide(args.first_number, args.second_number)
        else:
            # This should not happen due to argparse validation
            print(f"Error: Unsupported operator '{args.operator}'", file=sys.stderr)
            sys.exit(1)

        print(format_result(result))

    except ZeroDivisionError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except TypeError as e:
        print(f"Error: Invalid input - {str(e)}", file=sys.stderr)
        sys.exit(1)
    except ValueError as e:
        print(f"Error: Invalid input - {str(e)}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()