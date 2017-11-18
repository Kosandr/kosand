# kosand
Tool for managing kosandr sites and apps.


### Paths:


- THIS PATHS ARE ABSOLUTE AND ARE LAW. IF WANNA CHANGE ANYWHERE ELSE, FIRST CHANGE HERE

- TODO
   - instead of /sec/kosandr, do ~/orgs/Kosandr/kosand/ on host
   - /sec/ on VM
   - maybe mount data is separate directory in sec
      - host data for app and sites
         - /sec/kosandr/sites/data/{ro,rw}/{site,apps/<app-name>}
            - rw
               - rw/apps/<app-name>/{db,misc}
               - rw/site/{db,misc}
            - ro
               - ro/apps/<app-name>/{creds,nginx.conf}
               - ro/site/{creds,nginx.conf}
      - docker mounts
         - /sec/data/{ro,rw}/{site,apps/<app-name>}
            - rw
               - rw/apps/<app-name>/{db,misc}
               - rw/site/{db,misc}
            - ro
               - ro/apps/<app-name>/{creds,nginx.conf}
               - ro/site/{creds,nginx.conf}

- host to Docker mappings
   - host
      - /sec/kosandr/{sites/apps}
      - sites
         - /sec/kosandr/sites/<site-name>
      - apps
         - /sec/kosandr/apps/<app-name>/<app-version>

   - /sec/kosandr/sites/<site-name>/ ---> /sec/site/
      - site_conf.json        ---> /sec/site/site_conf.json
      - src                   ---> /sec/site/src (mounted ro)
      - data                  ---> /sec/site/data
         - data/db
         - data/creds
         - data/misc/{nginx.conf}
      - static                ---> /sec/static/site/{images,autogen,js,css}

   - /sec/kosandr/apps/<app-name>/<app-version>/
      - app_conf.json         ---> /sec/apps/<app-name>/<app_conf.json>
      - static                ---> /sec/static/apps/<app-name>/static/
         - images
         - autogen/{images,js,css}
         - js
         - css
      - src                   ---> /sec/apps/<app-name>/src
         - templates
         - jsx
         - sass
         - back
            - app.py
            - db.py
            - view.py
         -

   - docker VM
         - sites get mounted in /sec/site/src ro
         - apps get mounted in /sec/apps/<app-name>
         - assets get mounted in /sec/static/apps/<app-name>/<blah>
         - read-write data in /sec/site/data/

      - /sec/site <--- mounted in ro site code/templates
      - /sec/data/{db/creds/misc}





### Commands

kosand new-site <site-name>
   - creates site in /sec/kosandr/sites/<site-name>
      - /sec/kosandr/sites/<site-name>/{src/static/data}
         - data/{db/creds/nginx/misc}
            - nginx/nginx.conf
         - src/{back/templates/jsx/sass}
         - static/{images/autogen/js/css}



### Docker

- questions
   - how many instances?
      - 1 docker instance per site <-------
      - 1 docker instance for all sites
      - 0 docker instances
   - how to divide up the volumes?

- sites and apps options
   - every site has a copy of each app it uses
   - every site uses Unionfs to mount on top of apps?
   - every app is read-only, data stored in sites


=====================================


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
