


def gen_arg_parser():
   import argparse

   init_help = '''main actions:
      install           (global) install the global kosandr
      init (-a|-s) (-n <project-name>|--github <project-url>)
                        new site/app
      rm [(-a|-s) -n <project-name>]
                        delete site/app
      workon [-s -n <site-name>]
                        workon site; if no argument print current site
      install-app [--site-name <site-name>] --app-name <app-name>:<app-version>
                        install app to site
      uninstall-app [--site-name <site-name>] --app-name <app-name>
                        un-install app from site
      watch [(-s -n <site-name>|(-a -n <app-name>)]
                        watch project live
      start [-s -n <site-name>]
                        start running project
      stop [-s -n <site-name>]
                        stop running project
      status [-s -n <project-name>]
                        (local) print current status
      status --global   (global) status of all projects

      get [(-s|-a|-g)] [-p <project-name>] <config-name>
                        get configuration value. -s, -a and -g specify whether site app or global config
      set [(-s|-a|-g)] [-p <project-name>] <config-name> <config-val>
                        set configuration value

      =====old 1:

      app init -n <app-name>
                        new app
      app rm -n <app-name>
                        remove app
      site init -n <site-name>
                        new site
      site rm [-n <site-name>]
                        remove site
      site workon -n <site-name>
                        workon site
      site install-app [--site-name <site-name>] --app-name <app-name>:<app-version>
                        install app to site
      site watch [-n <site-name>]
                        watch project live
      site start [-n <site-name>]
                        start running project
      site stop [-n <site-name>]
                        stop running project
      site status [-n <site-name>]
                        (site local) print current status
      status            (global) status of all projects

      [(app|site)] get <config-name>
                        get configuration value
      [(app|site)] set <config-name> <config-val>
                        set configuration value
      =====end old 1

      =====old 2:
      new-app -p <app-name>
                        new app
      init -p <project-name>
                        new project
      setup             (project) run after cloning to setup
      rm [-n <project-name>]
                        remove current project from the list
      status [-p <project-name>]
                        (local) print current status
      status --global   (global) status of all projects

      =====end old 2

   '''

   p = parser = argparse.ArgumentParser(
         'kosand', epilog=init_help,
         formatter_class=argparse.RawTextHelpFormatter)


   #m_help_str = 'server mode (used with install): devel/prod'
   p_help_str = 'name of project'
   s_help_str = 'run command in site mode'
   a_help_str = 'run command in app mode'
   g_help_str = 'run command in global mode (used with status)'
   sn_help_str = 'site name (use with site install-app)'
   an_help_str = 'app name (use with site install-app)'
   gh_help_str = 'use github url to specify project source (used with init)'


   p.add_argument('-n', '--name', nargs='?', help=p_help_str)
   p.add_argument('-s', '--site', nargs='?', help=s_help_str)
   p.add_argument('-a', '--app', nargs='?', help=a_help_str)
   p.add_argument('-g', '--global', nargs='?', help=g_help_str)
   p.add_argument('-sn', '--site-name', nargs='?', help=sn_help_str)
   p.add_argument('-an', '--app-name', nargs='?', help=an_help_str)
   p.add_argument('-gh', '--github', nargs='?', help=gh_help_str)
   #p.add_argument('-g', '--global', help=g_help_str)
   #p.add_argument('-m', '--mode', nargs='?', help=m_help_str)

   choices = ['install', 'init', 'rm', 'workon', 'install-app', 'uninstall-app', 'watch', 'start', 'stop', 'status', 'set', 'get']
   p.add_argument('action', nargs='?', choices=choices)

   return parser

