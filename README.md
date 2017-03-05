# RoboLab Template

TODO: Description

## What's inside?

### ./src/

The directory for all source files that will be synced to the brick.

### ./src/main.py

This is the central hub for the execution of any code.

### ./deploy.py

Simple stub that calls the "real" deploy.py in the git submodule without an additional path prefix. Passes along any parameters without modification.

For usage, optional arguments, syntax, et cetera please refer to the submodule which should have already been initialized. To summarize, this script initiates the process of transmitting all source files present in the './src/' directory to a remote LEGO MINDSTORMS EV3 robot. Aftwards, the execution is started inside a tmux session from main.run() inside the main.py and the output is piped back to the host.


### ./robolab-deploy

The "real" deploy module. Git submodule
