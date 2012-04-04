#!/bin/sh
#
# A quick script to run musicdir from the source directory. You shouldn't use
# this script as an end-user. Instead, install musicdir with python setup.py install.
PYTHONPATH="$PYTHONPATH:musicdir" python scripts/musicdir $@
