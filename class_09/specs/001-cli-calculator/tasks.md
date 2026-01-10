# Tasks: CLI Calculator

**Feature**: CLI Calculator | **Branch**: `001-cli-calculator` | **Spec**: [specs/001-cli-calculator/spec.md](specs/001-cli-calculator/spec.md)
**Plan**: [specs/001-cli-calculator/plan.md](specs/001-cli-calculator/plan.md) | **Stage**: Implementation | **Date**: 2026-01-10

## Overview

Implementation of a command-line calculator that handles basic arithmetic operations (addition, subtraction, multiplication, division) with support for integer and decimal numbers, negative numbers, and proper error handling for edge cases like division by zero and invalid input.

## Phase 1: Setup Tasks

- [X] T001 Create project structure with src/ and tests/ directories
- [X] T002 Initialize pyproject.toml with required dependencies and configuration
- [X] T003 Set up virtual environment using uv package manager
- [X] T004 Create initial file structure for calculator module

## Phase 2: Foundational Tasks

- [X] T005 [P] Create calculator package structure with __init__.py files
- [X] T006 [P] Set up type checking configuration with mypy
- [X] T007 [P] Configure testing framework with pytest
- [X] T008 [P] Set up code formatting with black and linting with ruff

## Phase 3: User Story 1 - Basic Arithmetic Operations (Priority: P1)

- [ ] T009 [P] [US1] Implement Calculator class with basic arithmetic operations in src/calculator/core.py
- [ ] T010 [P] [US1] Add type hints to all calculator functions
- [ ] T011 [US1] Create CLI interface in src/calculator/cli.py using argparse
- [ ] T012 [US1] Implement argument parsing for two numbers and an operator
- [ ] T013 [US1] Connect CLI to calculator core functionality
- [ ] T014 [US1] Write unit tests for basic arithmetic operations in tests/unit/test_calculator.py
- [ ] T015 [US1] Write integration tests for CLI functionality in tests/integration/test_calculator_cli.py

## Phase 4: User Story 3 - Division by Zero Error Handling (Priority: P1)

- [ ] T016 [P] [US3] Implement division by zero error handling in calculator core
- [ ] T017 [US3] Create appropriate error message for division by zero
- [ ] T018 [US3] Ensure calculator exits gracefully with error code on division by zero
- [ ] T019 [US3] Write unit tests for division by zero scenario in tests/unit/test_calculator.py
- [ ] T020 [US3] Write integration tests for division by zero handling

## Phase 5: User Story 5 - Invalid Input Handling (Priority: P1)

- [ ] T021 [P] [US5] Implement validation for invalid operators (% not in +, -, *, /)
- [ ] T022 [US5] Implement validation for non-numeric input values
- [ ] T023 [US5] Create appropriate error messages for invalid input
- [ ] T024 [US5] Ensure calculator exits gracefully with error code on invalid input
- [ ] T025 [US5] Write unit tests for invalid input scenarios in tests/unit/test_calculator.py
- [ ] T026 [US5] Write integration tests for invalid input handling

## Phase 6: User Story 2 - Decimal Number Handling (Priority: P2)

- [ ] T027 [P] [US2] Enhance calculator to handle decimal numbers with appropriate precision
- [ ] T028 [US2] Update type hints to support float values properly
- [ ] T029 [US2] Write unit tests for decimal number operations in tests/unit/test_calculator.py
- [ ] T030 [US2] Verify floating point precision handling in calculations

## Phase 7: User Story 4 - Negative Number Support (Priority: P2)

- [ ] T031 [P] [US4] Update calculator to properly handle negative numbers in all operations
- [ ] T032 [US4] Enhance input parsing to recognize negative numbers
- [ ] T033 [US4] Write unit tests for negative number operations in tests/unit/test_calculator.py
- [ ] T034 [US4] Verify negative number handling in all arithmetic operations

## Phase 8: Polish & Cross-Cutting Concerns

- [ ] T035 [P] Run full test suite and achieve 90%+ coverage
- [ ] T036 [P] Run mypy type checking with no errors
- [ ] T037 [P] Format code with black and ensure no linting issues with ruff
- [ ] T038 [P] Test all acceptance scenarios from the feature spec
- [ ] T039 [P] Create/update README.md with usage instructions
- [ ] T040 [P] Verify command-line interface meets functional requirements FR-001 through FR-010

## Dependencies

- Setup tasks (Phase 1) must be completed before foundational tasks (Phase 2)
- Foundational tasks (Phase 2) must be completed before any user story tasks
- User Story 1 (Basic Operations) must be completed before User Stories 2, 4, and 5
- Core calculator functionality (US1) must be available before error handling (US3 and US5) can be fully integrated

## Parallel Execution Opportunities

- Within each user story, type hinting, implementation, and testing can often be done in parallel across different files
- Unit tests and integration tests can be developed in parallel for each feature
- Error handling implementations (US3 and US5) can be worked on simultaneously after core functionality exists

## Implementation Strategy

- Start with MVP: Implement basic arithmetic operations (US1) with minimal error handling
- Add decimal support (US2) and negative numbers (US4) as enhancements
- Implement robust error handling (US3 and US5) to ensure stability
- Follow test-first approach as required by constitution
- Maintain 90%+ test coverage throughout development