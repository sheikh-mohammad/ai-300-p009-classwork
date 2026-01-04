# Quickstart: CLI Calculator Development

## Prerequisites

- Python 3.10 or higher
- uv package manager (for dependency management as per constitution)

## Setup

### 1. Install uv (if not already installed)
```bash
# Install uv package manager
pip install uv
```

### 2. Clone and initialize the project
```bash
# Clone your repository
git clone <your-repo-url>
cd <repo-name>

# Create virtual environment with uv
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install dependencies
```bash
# Install dependencies with uv (no pyproject.toml yet, so create basic structure)
mkdir -p src/calculator tests/unit tests/integration
touch src/calculator/__init__.py
touch src/calculator/core.py
touch src/calculator/cli.py
```

### 4. Create pyproject.toml with required dependencies
```bash
# Create pyproject.toml file with basic configuration
cat > pyproject.toml << EOF
[project]
name = "cli-calculator"
version = "0.1.0"
description = "A command-line calculator"
readme = "README.md"
requires-python = ">=3.10"
dependencies = []

[tool.uv]
dev-dependencies = [
    "pytest>=7.0",
    "mypy>=0.990",
    "black>=22.0",
    "ruff>=0.0.244"
]

[project.scripts]
calculator = "calculator.cli:main"

[tool.mypy]
python_version = "3.10"
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true

[tool.ruff]
line-length = 88

[tool.black]
line-length = 88
EOF

# Install dependencies using uv
uv pip install -e .
```

## Development Commands

### Run the calculator
```bash
# After implementation, run the calculator:
python -m calculator.cli 5 + 3
# or if installed as a script:
calculator 5 + 3
```

### Run tests
```bash
# Run unit tests
python -m pytest tests/unit/

# Run all tests
python -m pytest tests/

# Run tests with coverage
python -m pytest --cov=src tests/
```

### Type checking
```bash
# Run mypy for type checking
python -m mypy src/
```

### Code formatting and linting
```bash
# Format code with black
python -m black src/ tests/

# Lint code with ruff
python -m ruff check src/ tests/
```

## Project Structure
```
src/
├── calculator/
│   ├── __init__.py
│   ├── core.py          # Main calculator logic with type hints
│   └── cli.py           # Command-line interface
│
tests/
├── unit/
│   ├── test_calculator.py    # Unit tests for calculator operations
│   └── test_cli.py           # Unit tests for CLI interface
└── integration/
    └── test_calculator_cli.py # Integration tests
```

## Implementation Roadmap

### Phase 1: Core Calculator Logic
1. Implement basic arithmetic operations in `src/calculator/core.py`
2. Add type hints to all functions
3. Write unit tests for all operations
4. Implement error handling for division by zero

### Phase 2: Command-Line Interface
1. Create CLI interface in `src/calculator/cli.py` using argparse
2. Parse command-line arguments
3. Validate input and handle errors gracefully
4. Write integration tests

### Phase 3: Testing and Validation
1. Ensure 90%+ test coverage as per constitution
2. Run type checking with mypy
3. Format code with black and lint with ruff
4. Test all acceptance scenarios from the feature spec