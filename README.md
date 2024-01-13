# widget-server

General purpose repo demoing an http server written in python. The server is a demo widget CRUD server.

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

TODO: frontend setup details, update Makefile as well

# usage

To start up the server:
```
make runserver
```

To start up the frontend:
```
make runfrontend
```

Run both of these commands to use the web application

# development

To run tests:
```
make test
```

To lint:
```
make lint
```

To format:
```
make format
```

To run mypy type checking:
```
make typing
```

More details can be found in the `Makefile` at the root of the project
