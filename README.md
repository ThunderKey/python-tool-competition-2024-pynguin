# Python Tool Competition Implementation Using Pynguin

Uses the python-tool-competition-2024 to generate tests using Pynguin.

For more information see
<https://github.com/ThunderKey/python-tool-competition-2024/>.

## Installation

This tool implementation requires *Python 3.10*
because [Pynguin](https://github.com/se2p/pynguin) only runs on Python 3.10 currently.
It will not run with any other Python version,
although the python-tool-competition supports a larger selection of Python versions.

To install this project you have to undertake the following steps:
* Install [poetry](https://python-poetry.org/)
* Run `poetry install`

## Development

The entry point called by `python-tool-competition-2024` is the `build_test`
method in `python_tool_competition_2024_pynguin/generator.py`.

## Configure Pynguin

Pynguin's configuration is set in the `_set_pynguin_configuration` function in
`python_tool_competition_2024_pynguin/generator.py`.
Check out [Pynguin's documentation](https://pynguin.readthedocs.io/en/latest/api.html#module-pynguin.configuration)
on the different configuration options to tune the tool.

## Calculating Metrics

Run `poetry run python-tool-competition-2024 run <generator name>`.

With `poetry run python-tool-competition-2024 run -h` you can find out what
generators were detected.

