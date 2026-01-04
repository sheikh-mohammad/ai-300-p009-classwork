# Data Model: CLI Calculator

## Core Entities

### Calculator Input
**Description**: Command-line arguments consisting of two numbers and an operator
**Fields**:
- `first_number`: float or int - The first operand in the calculation
- `operator`: str - The mathematical operation to perform ('+', '-', '*', '/')
- `second_number`: float or int - The second operand in the calculation

**Validation Rules**:
- `first_number` and `second_number` must be valid numeric values (int or float)
- `operator` must be one of the supported operators: '+', '-', '*', '/'
- `second_number` cannot be zero when operator is division ('/')

### Calculation Result
**Description**: The mathematical result of the operation performed on the two input numbers
**Fields**:
- `value`: float or int - The result of the calculation
- `formatted_output`: str - The string representation of the result for display

**Validation Rules**:
- Must be a valid number (no infinity or NaN values)
- Should maintain appropriate precision for decimal calculations

### Error Message
**Description**: A user-friendly message displayed when invalid input is provided or an error occurs
**Fields**:
- `error_type`: str - The category of error (e.g., 'DIVISION_BY_ZERO', 'INVALID_INPUT', 'INVALID_OPERATOR')
- `message`: str - The human-readable error message to display to the user
- `exit_code`: int - The exit code to return to the command line (non-zero for errors)

**Validation Rules**:
- `message` must be non-empty and user-friendly
- `exit_code` must be a valid exit code (typically non-zero for errors)

## State Transitions

### Calculator Operation Flow
1. **Input Validation State**: Input is parsed and validated
   - On valid input → Calculation State
   - On invalid input → Error State

2. **Calculation State**: Mathematical operation is performed
   - On successful calculation → Result Output State
   - On mathematical error (e.g., division by zero) → Error State

3. **Result Output State**: Result is formatted and displayed
   - Always transitions to Exit State

4. **Error State**: Error message is formatted and displayed
   - Always transitions to Exit State

5. **Exit State**: Program terminates with appropriate exit code

## Relationships

- Calculator Input is processed to produce a Calculation Result or Error Message
- Calculator Input validation may result in an Error Message instead of a Calculation Result
- Both Calculation Result and Error Message lead to program termination with appropriate exit codes