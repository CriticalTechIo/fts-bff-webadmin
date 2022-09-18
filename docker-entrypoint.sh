#!/bin/sh

set -e

# activate our virtual environment here
. /venv/bin/activate && pip install *.whl

# You can put other setup logic here

# Evaluating passed command:
exec "$@"
