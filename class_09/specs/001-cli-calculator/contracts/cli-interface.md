# CLI Interface Contract: Calculator

## Command Format
```
calculator <number1> <operator> <number2>
```

## Parameters

### number1
- **Type**: Numeric (int or float)
- **Description**: The first operand for the calculation
- **Required**: Yes
- **Validation**: Must be a valid number (positive, negative, or decimal)

### operator
- **Type**: String
- **Description**: The mathematical operation to perform
- **Required**: Yes
- **Valid Values**: `+`, `-`, `*`, `/`
- **Validation**: Must be one of the supported operators

### number2
- **Type**: Numeric (int or float)
- **Description**: The second operand for the calculation
- **Required**: Yes
- **Validation**: Must be a valid number; cannot be zero when operator is division

## Return Values

### Success
- **Exit Code**: 0
- **Output**: The result of the calculation as a number
- **Example**: `calculator 5 + 3` outputs `8`

### Error Cases

#### Invalid Operator
- **Exit Code**: 1
- **Output**: "Error: Invalid operator - only +, -, *, / are supported"

#### Division by Zero
- **Exit Code**: 2
- **Output**: "Error: Division by zero is not allowed"

#### Invalid Input
- **Exit Code**: 3
- **Output**: "Error: Invalid input - please provide valid numbers"

## Examples

```
calculator 10 + 5     # Output: 15
calculator 10 - 4     # Output: 6
calculator 6 * 7      # Output: 42
calculator 15 / 3     # Output: 5.0
calculator 5.5 + 2.3  # Output: 7.8
calculator -5 + 3     # Output: -2
calculator -10 * -2   # Output: 20
calculator 10 / 0     # Output: Error: Division by zero is not allowed
calculator abc + def  # Output: Error: Invalid input - please provide valid numbers
calculator 5 % 3      # Output: Error: Invalid operator - only +, -, *, / are supported
```

## Error Codes

- `0`: Success - calculation completed successfully
- `1`: Invalid operator
- `2`: Division by zero
- `3`: Invalid input
- `4`: Wrong number of arguments