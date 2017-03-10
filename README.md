# kosand
Tool for managing kosandr sites and apps.

Usage example
```bash


kosand install -m devel/prod = install kosand system-wide
kosand init -p test = initialize project test

Usage old
```bash

kosand start [foreground/fg]
   start daemon
kosand stop
   stop background daemon

kosand restart

kosand setup

kosand init <sitename>
   new website
kosand new-app <appname>
   make new app
kosand install-app

kosandr prompt on
kosandr prompt off

```

kosand deps
   pip install demonize

   pydagger
      VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3 /usr/local/bin/virtualenvwrapper.sh


Style guide:
```
no tab characters. use 3 spaces for tabbing

functions use underscore format: func_name()
classes and variables use camelCase: someVar

functions and variables begin with lower-case letter
classes begin with capital letter

```
