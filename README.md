# Cheap Stocks Inc

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/ae155b86e7324292995b7b9a7bc70136)](https://app.codacy.com/manual/wambuguedison/cheap-stocks-inc?utm_source=github.com&utm_medium=referral&utm_content=wambuguedison/cheap-stocks-inc&utm_campaign=Badge_Grade_Dashboard)
[![repo_size](https://img.shields.io/github/repo-size/wambuguedison/cheap-stocks-inc?style=plastic)]()
[![last_commit](https://img.shields.io/github/last-commit/wambuguedison/cheap-stocks-inc)]()

A command line application centered around stocks that will be used by users in Africa.

#### About

This is a command line application that takes in currency (using ISO 4217 code) as an argument and displays whether or not the currency is supported in the application.

#### Implementation

This tool has been implemented using python 3.8.5

#### How to Install

Install python from [here](https://www.python.org/downloads/release/python-385/)

```bash
pip install virtualenv
virtualenv env
. venv/bin/activate #Linux or OsX
venv\scripts\activate #Windows
pip install -r requirements.txt
pip install --editable .
```

#### Usage

```bash
cheap-stocks currency #where 'currency' is the ISO 4217 code
```

**Help**

```bash
cheap-stocks --help
```
