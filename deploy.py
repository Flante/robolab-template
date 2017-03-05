#!/usr/bin/python3

"""
Simple stub that calls the 'real' deploy.py in the git submodule without an additional path prefix. Passes along any parameters without modification.

For usage, optional arguments, syntax, et cetera please refer to the submodule which should have already been initialized. To summarize, this script initiates the process of transmitting all source files present in the './src/' directory to a remote LEGO MINDSTORMS EV3 robot. Aftwards, the execution is started inside a tmux session from main.run() inside the main.py and the output is piped back to the host.

This module: https://github.com/7HAL32/robolab-template
The submodule: https://github.com/7HAL32/robolab-deploy

Part of the RoboLab project at the Systems Engineering Group, TU Dresden.
"""

import sys
from subprocess import call

# it's basically a one-liner \o/
process = call(['./robolab-deploy/test.py'] + sys.argv[1:])
