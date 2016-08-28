# Python Installation
This folder has a few basic examples to get you started with python. There are
2 widely used different versions of python, python 2 and python 3. I will be
using python 3, but most examples should work either way.

## Check for python installation
Python may come with your system, check using the following
commands:
```
$ python
$ python3
$ py
```
If none of them work it probably means you don't have
python installed.

## Installing python
### Mac install
Install brew: [brew.sh](http://brew.sh)

Use brew to install python:
```
$ brew update
$ brew upgrade
$ brew install python
$ brew install python3
```
(It can be useful to install both versions of python)

### Ubuntu install
TODO

### Windows install
Download python from python.org/downloads/. Enable the
option to add executable to PATH variable in the installer.
The last version you install will be default. To launch
python, use the launcher(py.exe) from cmd or powershell:
```
$ py
```
To launch a specific version:
```
$ py -3
$ py -2.7
```

## PIP
### Installing python packages
python includes pip, a tool (package manager) for installing python
libraries/packages. It should be accessible anywhere by running the command:
```
$ pip install <package name>
or
$ pip3 install <package name>
```
### Checking pip version
It's a good idea to check that pip and pip3 commands are installed for
the python installation you intend:
```
$ pip -V
pip 8.1.2 from /usr/local/lib/python2.7/site-packages (python 2.7)
$ pip3 -V
pip 8.1.2 from /usr/local/lib/python3.5/site-packages (python 3.5)
```
(pip will install packages for version 2.7, pip3 will install packages for 3.5).
### What packages to download:
Some example packages you will probably need:
```
$ pip install numpy scipy matplotlib argparse
$ pip3 install numpy scipy matplotlib argparse
```
### Downloading packages for one of many python versions
If you have multiple python versions installed, and cannot get pip to install
a package for your version this can be useful:
```
$ python3 -m pip install numpy
```
Also useful when using the py launcher for different versions:
```
$ py -2.6 pip install numpy
```
This will install numpy for my pthon 2.6 installation, even though the default
"python" command starts python 2.7.

## Running python interactive interpreter
After a successful install running python should be as simple as:
```
$ python
or
$ python3
```
On my machine:
```
$ python
Python 2.7.12 (default, Aug 20 2016, 13:01:52)
[GCC 4.2.1 Compatible Apple LLVM 7.3.0 (clang-703.0.31)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
```
As you can see I have python 2.7.12 installed currently. Type *exit()* to exit
the python interpreter. On UNIX systems EOF (Ctrl-D) also works.

I also have python 3.5.2 installed:
```
$ python3
Python 3.5.2 (default, Aug 20 2016, 14:09:43)
[GCC 4.2.1 Compatible Apple LLVM 7.3.0 (clang-703.0.31)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

## Running python scripts
Run a python script by supplying the file name as a command line argument:
```
$ python test.py
or
$ python3 test.py
```
This will execute the script you have written in test.py!
