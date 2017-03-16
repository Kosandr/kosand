# ROADPATH

- [ ] implement kosand.conf generator and internal state trackers
- [ ] tool features
   - [ ] project auto-pick a port
   - [ ] setters/getters
- [ ] generate install_dir manually
- [ ] watcher/compiler scripts
- [ ] assets
   - [ ] git repo as a sub-module
   - [ ] auto-generate different image sizes

# PROBLEMS

- [ ] not using os.path.join
- [ ] complete crap without docker
   - [ ] nginx parser deletes comments
- [ ] installer.py has all the /sec paths hardcoded

# TODO
add needed packages in installer.py

nginx.conf for each site
add site to global kosand list (stored in sec)


***======commands
kosand install = (global) install/set-up kosand

kosand init -p <project-name> = initialize new project

kosand setup = take existing project (after cloning) and set it up

kosand rm <project-name> = remove project

kosand watch <project-name> = (devel) watch current project live

kosand start <project-name> = start runnning in background

kosand stop <project-name> = stop the project

kosand status [-p <project-name>] = print global status or for specific project

======commands TODO

==get/set/update

kosand get [--global] [conf-var-name] = by default, lists possible getting variables

kosand set [--global] [conf-var-name] [conf-var-val] = by default, sets possible variables

==update
kosand update PipPackages
kosand update NpmPackages

==workon

kosand workon <project-name>

==assets
kosand [-p <project-name>] --upload-assets = upload assets

OR

kosand assets [upload/download/snapshot]

======old

kosand setup = setup project name
kosand update = ????
kosand run = run the current project
kosand status = current status
kosand assets --download = (download should be part of setup)


***======usage examples


***======notes:
- instead of files, can use SQLite to keep track of all the data
- security
   - container/docker?
   - filesystem users/permissions
      - user for each site/project?
   - MySQL users/permissions

kosand status --global
   running/stopped/dead

***======dir layout:
   /sec/admin_scripts = admin scripts
      TODO: maybe remove
   /sec/backups = has backup data
      TODO: maybe remove
   /sec/creds = credentials
      /sec/creds/global = global creds
      /sec/creds/local  = has a dir with each project name and local credentials
      TODO: think of a way to sync them easily when setting up new server
   /sec/db = databases
   /sec/is_prod = is production?
   /sec/logs = log data
   /sec/misc = miscalleneous files
   /sec/internal = kosand internal files
      /sec/internal/sites-backend = backend code for each site
   /sec/projects = original source code for each project
   /sec/www-data = nginx data


