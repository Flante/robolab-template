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
import platform
import subprocess

# windows needs some special attention
# but apart from that it's basically a one-lineer \o/
OS = platform.system()
if OS is "Windows":
    # the shebang won't work
    # therefore, we take the name of the python3 executable in the systems PATH
    # alternatively: direct full path to the executable
    # as of March 2017 this should usually be "python"
    PYHON_PATH = 'python'
    process = subprocess.call([PYHON_PATH, './robolab-deploy/deploy.py'] + sys.argv[1:])
else:
    process = subprocess.call(['./robolab-deploy/deploy.py'] + sys.argv[1:])
