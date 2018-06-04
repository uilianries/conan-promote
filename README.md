# Conan Promote

A tool to promote a Conan package on stable channel

### Introduction

To solve a centralized and stable channel for Conan packages,  
this script will help to promote any package reference as stable on conan server.

### Remotes

There are some ways to add on remote:

Adding manually:

    $ conan remote add bintray https://api.bintray.com/conan/<user>/<conan-repo>

Or, by `conan config`:

    $ conan config install http://github.com/bincrafters/conan-config.git

### Install

To install Conan promote in your local machine:

    $ clone http://github.com/uilianries/conan-promote.git
    $ cd conan-promote
    # pip install .

### Distribute

To distribute the package as tar file:

    $ clone http://github.com/uilianries/conan-promote.git
    $ cd conan-promote
    # python setup.py sdist

### Usage

```
usage: conan-promote [-h] [-c CHANNEL] [-l LOGIN_USER] [-u USER] [-r REMOTE] [-V] [-v] [reference]

Promote Conan package to stable channel

positional arguments:
  reference             Reference name to be promoted, e.g: "OpenSSL/1.0.2@user/ci"

optional arguments:
  -h, --help            show this help message and exit
  -c CHANNEL, --channel CHANNEL Stable channel name
  -l LOGIN_USER, --login-user LOGIN_USER Username login to push on stable channel
  -u USER, --user USER  Username to be applied on package name
  -r REMOTE, --remote REMOTE Remote server name
  -V, --verbose         Enable verbose message
  -v, --version         Show version
  -s SOURCE, --source SOURCE Download the package from this remote
```

### Examples

To promote a package on stable channel:

E.g: Promote *foobar/0.1.0@qux/ci* as *foobar/0.1.0@user/stable*:

    $ conan-promote foobar/0.1.0@qux/ci

E.g: Promote *foobar/0.1.0@qux/ci* as *foobar/0.1.0@user/stable* and rename the target remote to *gitlab*:

    $ conan-promote foobar/0.1.0@qux/ci -r gitlab

E.g: Promote *foobar/0.1.0@qux/ci* as *foobar/0.1.0@user/release*:

    $ conan-promote foobar/0.1.0@qux/ci -c release

E.g: Promote *foobar/0.1.0@qux/ci* as *foobar/0.1.0@user/stable* and login on remote as *betinho*:

    $ conan-promote foobar/0.1.0@qux/ci -l betinho

E.g: Promote *foobar/0.1.0@qux/ci* as *foobar/0.1.0@conan/stable*:

    $ conan-promote foobar/0.1.0@qux/ci -u conan

E.g: Promote *OpenSSL/1.0.2@conan/stable* from *conan-center* as *OpenSSL/1.0.2@user/stable* to *user*:

    $ conan-promote OpenSSL/1.0.2@conan/stable -s conan-center

### Development

To develop, fix or improve this project, it's recommend to install all dev dependencies:

    # pip install -r conan/requirements_dev.txt

Also, **pylint** should be used to get a score == 10.0

### Test

To execute all tests:

    $ nosetests .


### LICENSE
[MIT](LICENSE.md)
