<!--
Sync Impact Report:
- Version change: N/A → 1.0.0 (initial creation)
- Added sections: All principles and governance for Python calculator project
- Templates requiring updates: N/A (no changes needed to existing templates)
- Follow-up TODOs: None
-->
# Python Calculator Constitution

## Core Principles

### I. Type Safety First
All code MUST use type hints for functions, methods, variables, and class attributes. Static type checking with mypy is mandatory before merging any changes. This ensures code clarity, prevents runtime errors, and improves maintainability.

### II. Dependency Management with uv
The project MUST use uv for dependency management and virtual environment creation. All dependencies must be explicitly declared in pyproject.toml with version constraints. No manual pip installations allowed in development workflow.

### III. Test-First (NON-NEGOTIABLE)
All calculator functionality must have corresponding unit tests written before implementation. Tests must cover normal operations, edge cases, and error conditions. Test coverage must be maintained at 90% or higher for all calculator operations.

### IV. Minimal Viable Calculator
Start with basic arithmetic operations (+, -, *, /) and expand incrementally. No premature feature addition - implement only what is necessary for core calculator functionality. Follow YAGNI (You Aren't Gonna Need It) principle.

### V. Error Handling and Validation
Calculator must handle all mathematical edge cases including division by zero, overflow conditions, and invalid inputs. All error states must be explicitly handled with clear, user-friendly error messages.

### VI. Command-Line First Interface
Calculator functionality must be accessible via command-line interface as the primary interaction method. Input validation and formatted output are required for all CLI operations.

## Technology Stack Requirements

- **Language**: Python 3.10+ with strict type hints
- **Dependency Manager**: uv for all package management
- **Testing**: pytest with coverage reporting
- **Type Checking**: mypy with strict mode enabled
- **Formatting**: black for code formatting, isort for import sorting
- **Linting**: ruff for linting and code quality checks

## Development Workflow

- All code changes require passing type checks, linting, and tests
- Pull requests must include appropriate tests for new functionality
- Code review must verify type hint completeness and correctness
- Changes must not break existing functionality or tests
- Documentation updates required for all public APIs

## Governance

This constitution governs all development decisions for the Python calculator project. All PRs and code reviews must verify compliance with these principles. Changes to this constitution require explicit approval and documentation of the rationale. Use this constitution as the primary reference for development decisions and quality standards.

**Version**: 1.0.0 | **Ratified**: 2026-01-04 | **Last Amended**: 2026-01-04