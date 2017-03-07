# RoboLab Template

Template repository for the RoboLab courses conducted in spring and autumn by the Systems Engineering Group at the Department of Computer Science, TU Dresden.

Contains a deploy script that syncs Python files from the local `src/` folder to a remote LEGO
MINDSTORMS EV3 brick running the customized operating system [ev3dev-robolab](https://github.com/7HAL32/ev3dev-robolab). The script is included by the submodule [https://github.com/7HAL32/robolab-deploy](robolab-deploy).
Afterwards this scripts attaches to a pre-loaded tmux session running `python3.6` including
some imported modules, performs a reload on the `main.py` file in the
`/home/robot/src/` folder and starts execution from `main.run()`. This functionality on the remote client is provided by the systemd service [ev3-robolab-startup](https://github.com/7HAL32/ev3-robolab-startup). Also comes with a simple example `main.py` file that prints `Hello World!`.

## Installation

These steps should be only performed by **one** member of your group.

1. Clone the repository to any local destination.

 ```
git clone --recursive https://github.com/7HAL32/robolab-template
```
 The flag `--recursive` initializes the submodule `robolab-deploy`.

2. Set the remote upstream to your group repository.

 ```
git remote set-URL origin https://bitbucket.org/robolab-<season>-<year>/group-<id>
```

 `<season>` is either `spring` or `autumn` depending on which RoboLab course you are participating in, i.e. Spring Course (INF) or Autumn Course (NES).

 `<year>` is the year your course has started in the format `yy`. For instance if the introduction took place on March 06th, 2017 `<year>` will be `17`.

 `<id>` has been assigned to you at the beginning of the course. Please make sure to include leading zeros and fill up the id to three digits, e.g. group 42 will enter `042`.

3. Verify, if the new upstream has been set successfully.

 ```
 git remote -v
 ```

4. Perform an initial push.

 ```
 git push origin master
 ```

Now the other members of your team are ready to clone your group repository. Make sure to enter the corresponding URL from step (2).

## Dependencies

In order to function you will need to have [Python 3.6](https://www.python.org/downloads/) installed. All other auxiliary files will be downloaded by the script itself. On Linux you may also need to install [sshpass](https://gist.github.com/arunoda/7790979) manually.

**Make sure that you are connected to the campus network on the first run, in order to fetch all dependencies.**

## Usage

All source file must reside inside the `src/` sub directory. To start the process of deploying and executing call the file according to your operating system and setup of Python.

#### Linux and macOS

```
./deploy.py [optional arguments]
```

#### Windows

```
PYTHON_EXECUTABLE ./deploy.py [optional arguments]
```
Where `PYTHON_EXECUTABLE` contains either the shortcut registered in your systems `$PATH` environment or the full direct path to the `python.exe`.

For usage, optional arguments, syntax, et cetera simply call it with the `--help`.

## What's inside?

### ./src/

Directory for all source files that will be synced to the brick.

### ./src/main.py

Central hub for the execution of any code.

The deploy script will call the function `main.run()`. Make sure that all modules are imported in this file and are called appropriately from within `run()`.

### ./deploy.py

Simple stub that calls the "real" `deploy.py` in the git submodule without an additional path prefix and passes along any parameters without modification.

### ./robolab-deploy/

Contains the "real" deploy module, including configuration files, scripts and necessary auxiliary binaries like `putty` and `pscp`.

## Credits

Contributors: Felix Döring, Paul Genssler, Lutz Thies and Felix Wittwer.

Developed as a part of the RoboLab project at the Systems Engineering Group, Department of Computer Science, TU Dresden.

Copyright &copy; 2017 Lutz Thies
