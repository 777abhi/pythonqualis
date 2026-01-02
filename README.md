# Python Testing & Concepts Playground

## Project Overview

This repository is a comprehensive collection of Python examples designed to demonstrate various testing frameworks, Object-Oriented Programming (OOP) concepts, and core language features. It serves as a reference for developers looking to learn or refresh their knowledge on Python's testing ecosystem and fundamental programming patterns.

## Project Structure

The repository is organized into the following key directories:

- **`Project/`**: Contains a sample "Inventory" project with associated tests, demonstrating a real-world testing scenario. This directory is structured as a Python package.
  - `proj/`: Source code for the sample project (`MobileInventory` class).
  - `test/`: Tests for the sample project.
- **`py3oop/`**: Dedicated to Python 3 Object-Oriented Programming examples.
- **`unittest/`**: specific examples utilizing the `unittest` framework.
- **`junit/`**: Directory for storing test results in JUnit format.
- **Root Directory**: Contains various standalone scripts covering generators, basic utilities, and class exercises.

## Features

### 1. Testing Frameworks
The project showcases usage examples for multiple Python testing frameworks:
- **`unittest`**: The standard library testing framework.
- **`pytest`**: A popular, feature-rich third-party testing framework.
- **`nose`**: Examples for the nose testing framework.
  > **Note:** `nose` is in maintenance mode and may not be compatible with newer Python versions (e.g., Python 3.12+). Use `pytest` or `unittest` for new projects.
- **`doctest`**: Demonstrations of testing within docstrings.

### 2. Core Python Concepts
- **Object-Oriented Programming**: Examples like `ClassesObjects1.py` and the `py3oop/` directory cover class definitions, magic methods (`__init__`, `__str__`, `__add__`), and inheritance.
- **Generators**: `FactorialGenerator.py` and `FibonacciGenerator.py` illustrate how to create and use Python generators.
- **Utilities**: Scripts like `calender.py`, `evenodd.py`, and `os.py` provide basic utility examples.

### 3. CI/CD Integration
- **Azure Pipelines**: Includes `azure-pipelines.yml` configuration for continuous integration.

## Usage

### Installation
Ensure you have Python installed. Install the required dependencies using:

```bash
pip install -r requirements.txt
```

### Running Tests

You can run tests using different frameworks as shown below:

#### Using `unittest`
```bash
python -m unittest discover -v
# Or specific modules
python -m unittest unittest/unittest1.py
```

#### Using `pytest`
```bash
# Run all tests
pytest -v

# Run specific test file
pytest -v Project/test/test_inventory.py
```

#### Using `doctest`
```bash
python -m doctest -v evenodd.py
```

### Running Scripts
To run any of the standalone scripts, simply execute them with python:
```bash
python FibonacciGenerator.py
python ClassesObjects1.py
```

## Future Roadmap & Incremental Improvements

To further enhance this project, the following incremental improvements can be made:

1.  **Expand Test Coverage**: Add more comprehensive test cases for the `Inventory` project, including edge cases and integration tests.
2.  **Modernize Testing**: Refactor tests to use `pytest` fixtures and parameterization for cleaner and more maintainable code.
3.  **Code Quality Tools**: Integrate linters (`flake8`, `pylint`) and formatters (`black`) to enforce code style and quality.
4.  **GitHub Actions**: Add a `.github/workflows/main.yml` to support GitHub Actions for CI/CD, providing an alternative to Azure Pipelines.
5.  **Documentation**: Add docstrings to all functions and classes, and potentially set up Sphinx to generate professional documentation.
6.  **Advanced Topics**: Add examples for Python decorators, context managers, and async/await programming.
7.  **Clean up Legacy Code**: Migrate away from `nose` and ensure all scripts are compatible with the latest Python versions.
