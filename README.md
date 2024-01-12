# data-playground

General purpose repo for ad-hoc data analysis. This repo is intended to be forked and modified for specific use cases as needed.

# setup

This repo expects `python 3.11.x`; ensure `pip3` is tied to this version of python.
[poetry](https://python-poetry.org/) is used for dependency managment.

To install poetry and dependencies, run
```
make install
```

To add a python package, run

```
poetry add $PACKAGE_NAME
```

# structure

* Use `./data_playground` for imported python module code
* Use `./notebooks` for ad-hoc data analysis


# usage

To start up the notebook server, run
```
make notebook
```
