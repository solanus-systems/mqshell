# mqshell

[![ci](https://github.com/solanus-systems/mqshell/actions/workflows/ci.yml/badge.svg)](https://github.com/solanus-systems/mqshell/actions/workflows/ci.yml)

A python command-line interface for interacting with micropython devices running [mqterm](https://github.com/solanus-systems/mqterm).

Inspired by [mqboard](https://github.com/tve/mqboard).

## Usage

TODO

## Developing

You need python and a build of micropython with `asyncio` support. Follow the steps in the CI workflow to get a `micropython` binary and add it to your `PATH`.

Before making changes, install the development (CPython) dependencies:

```bash
pip install -r dev-requirements.txt
```

### Linting

This project uses [ruff](https://github.com/astral-sh/ruff) for linting. After making changes, you can run the linter:

```bash
ruff check
```

### Testing

Before running tests, install the test (micropython) dependencies:

```bash
./bin/setup
```

#### Unit tests

You can run the unit tests using `unittest`:

```bash
python -m unittest
```

#### Integration tests

Integration tests use a running MQTT broker ([mosquitto](https://mosquitto.org/)), which you need to have installed (e.g. with `brew`).

There is a script that will set up the test environment, run the tests, and tear down the broker afterward:

```bash
./bin/test_e2e
```

Sometimes it's useful to debug an individual integration test. To do this, you need to run the broker yourself, then set up the environment and invoke the test directly:

```bash
mosquitto -v  # keep open to check the broker logs
```

Then in another terminal:

```bash
python ./tests/e2e/e2e_foo.py
```

## Releasing

To release a new version, commit your changes and make a pull request. After merging, create a new tag and push to GitHub:

```bash
git tag vX.Y.Z
git push --tags
```
