# py-stats-toolkit (TDD Learning Project)

## Project Overview
This repository houses a personal project primarily focused on learning and applying Test-Driven Development (TDD) principles to the creation of statistical computation functions. It also serves as a sandbox for exploring Python packaging, broader testing methodologies, and refactoring techniques

## Features

* **Statistical Functions:** Core functions for common statistical calculations (e.g., mean, standard deviation).
* **Test-Driven Development:** Developed with a strong emphasis on writing tests *before* implementation.
* **Python Packaging Practice:** Structured as a Python package to learn best practices for distribution.

## Project Structure

The key components are:
* `py_stats_toolkit/`: The main Python package containing the statistical computation logic.
* `tests/`: Contains unit tests for the functions in `py_stats_toolkit`.
* `pyproject.toml`: Defines the project metadata and build system.

## Installation (Local Development)

This project is intended for local development and learning.

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/ScriptsAndData/py-stats-toolkit.git
    cd py-stats-toolkit
    ```

2.  **Create and activate a virtual environment** (highly recommended):
    ```bash
    python -m venv py310env
    source py310env/bin/activate  # On Linux/macOS
    # py310env\Scripts\activate   # On Windows
    ```

3.  **Install project in editable mode** (optional, but good for development):
    This allows you to import `py_stats_toolkit` as a package.
    ```bash
    pip install -e .
    ```

## Usage

Once installed, you can import and use the statistical functions in your Python scripts or interactive sessions.

```python
# Example of using the package
from py_stats_toolkit import calculate_mean, calculate_std_dev

data = [10, 20, 30, 40, 50]
mean_val = calculate_mean(data)
std_dev_val = calculate_std_dev(data)

print(f"Mean: {mean_val}")
print(f"Standard Deviation: {std_dev_val}")
