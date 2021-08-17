# Introduction <!-- omit in toc -->
This is a code repo template for code using a command line interface
- [Description](#description)
- [Install code](#install-code)
- [How to use the code](#how-to-use-the-code)
  - [How to run code](#how-to-run-code)
  - [How to run tests](#how-to-run-tests)
- [Folder structure](#folder-structure)


# Description
The code does not have functional use.
However, the template covers:
1. Code directory layout
2. Command line interface using "Argh"
3. Progressbar / Parallel processing using progressbar, "tqdm"
4. Testing using "pytest"
5. Requirements file
6. Documentation

Starting with this template should make an initial code repo setup faster and easier.

# Install code
This guide assumes you are using windows, the instructions should be similar for other operating systems.
Its assumed that you are using [vscode and have python installed](https://code.visualstudio.com/docs/python/python-tutorial).

1. Download/clone the code (where this readme is located)
2. Open vscode and from within vscode open the main folder with the code
3. Open a new terminal
   1. Press: Ctrl+Shift+P and type "terminal"
   2. Select: Python: create terminal
4. In the new terminal create a new environment and activate it
   1. 'python -m venv .venv'
   2. If prompted, click yes to use the new virtual environment
   3. If not prompted, click the python/environment button i the bottom left of the blue ribbon and select the new environment
   4. Ensure that the correct environment is activated, you should see the following in the terminal
      1. `([env_name]) folderpath]>`
      2. `(.venv) C:\Users\testuser>`
5.  Install the requirements file.
   * **Ensure that you are in the correct directory and using the "[env_name]" environment**
   * Run: `pip install -r requirements.txt`
6.  Done! you can now move on to the next section on [how to use the code](#how-to-use-the-code)

# How to use the code
* Pre-requisites
  1. Ensure that you have followed all the steps to [Install code](#install-code)
  2. Ensure that you have activated the correct virtual environment.
  3. Ensure that the dependencies in requirements.txt are installed.
  4. Ensure that you have navigated to the directory containing this code.

## How to run code
Use the command line
1. Get help
    * `python main.py -h`
2. Get version information
    * `python main.py version`
    * `python main.py version -h`
3. Run the main entry point
    * `python main.py entry 5`
    * `python main.py entry 5 --y 10`
    * `python main.py entry -h`

## How to run tests
Use the command line
1. Run all tests
    * `pytest`
2. Run all tests in specific folder
    * `pytest tests/unit`
3. Run all tests in specific test file
    * `pytest tests/unit/src/test_myprojectcode.py`
4. Run single specific test in file
    * `pytest tests/unit/src/test_myprojectcode.py::test_is_even`

# Folder structure
Describe the folder structure and file content

+ <details>
    <summary> Template code - The main directory of the template </summary>

    + <details>
        <summary> src - The source code </summary>

        * [__ init __.py](/src/__init__.py) - Empty init file
        * [about.py](/src/about.py) - File with version information and change log
        * [myprojectcode.py](/src/myprojectcode.py) - The main project code file
        * [utils.py](/src/utils.py) - Utility functions and methods used by the main
        </details>

    + <details>
        <summary> tests - Code for tests </summary>

        + <details>
            <summary> integration - Code for integration tests </summary>

            + <details>
                <summary> src - Integration tests for the code in src </summary>

                * [__ init __.py](/src/__init__.py) - Empty init file
                </details>

            * [__ init __.py](/src/__init__.py) - Empty init file
            </details>

        + <details>
            <summary> unit - Code for unit tests </summary>

            + <details>
                <summary> src - Unit tests for the code in src </summary>

                * [__ init __.py](/src/__init__.py) - Empty init file
                * [test_myprojectcode.py](/src/test_myprojectcode) - unit tests
                </details>

            * [__ init __.py](/src/__init__.py) - Empty init file
            </details>

        * [__ init __.py](/src/__init__.py) - Empty init file
        * [conftest.py](/tests/conftest.py) - File containing pytest fixtures and configurations
        </details>

    * [main.py](/main.py) - The entry point of the code
    * [README.md](/README.md) - The project documentation
    * [requirements.txt](/requirements.txt) - The code dependencies/requirements
    * [template_log.log](/template_log.log) - The output log of the code

    </details>
