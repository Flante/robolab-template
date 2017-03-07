#!/usr/bin/python3

"""
Simple stub that calls the 'real' deploy.py in the git submodule without an
additional path prefix. Passes along any parameters without modification.

To summarize, this script initiates the process of transmitting all source files
present in the './src/' directory to a remote LEGO MINDSTORMS EV3 robot.
Aftwards, the execution is started inside a tmux session from main.run() inside
the main.py and the output is piped back to the host. This requires the systemd
unit ev3-robolab-startup.service to be installed and enabled on the target
device.

For usage, optional arguments, syntax, et cetera please refer to the
"robolab-deploy" submodule which should have already been initialized.

This module: https://github.com/7HAL32/robolab-template
The submodule: https://github.com/7HAL32/robolab-deploy

Developed as a part of the RoboLab project at TU Dresden.
(c) 2017 Lutz Thies
"""

import sys
import subprocess

# get the full executable path, because windows can't handle our shebang
PYTHON_EXECUTABLE = sys.executable
# it's basically a one-liner \o/
subprocess.call([PYTHON_EXECUTABLE, './robolab-deploy/deploy.py'] + sys.argv[1:])
