#!/bin/sh
poetry install
poetry run pre-commit install && poetry run pre-commit install --hook-type commit-msg
poetry run pre-commit run --all-files
