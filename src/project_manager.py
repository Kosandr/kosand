import settings, os
from utiltools import shellutils

sh_get_path = shellutils.get_abs_path_relative_to
kosandDir = sh_get_path(os.path.realpath(__file__), '..')

def execWithVirtEnv(cmd):
   sourceVirtEnv = 'source `which virtualenvwrapper.sh`; '
   os.system('bash -c "%s %s"' % (sourceVirtEnv, cmd))

def new_project(projectName):
   config_raw = settings.gen_new_conf(projectName)

   config = settings.get_conf_data(config_raw)
   #print(config)

   projectSettings = config['ProjectSettings']

   jsxDir = projectSettings['JsxDir']
   pyDir = projectSettings['PyDir']
   sassDir = projectSettings['SassDir']
   templatesDir = projectSettings['TemplatesDir']
   staticDir = projectSettings['StaticDir']

   for dir_path in [jsxDir, pyDir, sassDir, templatesDir, staticDir]:
      os.system('mkdir -p ' + dir_path)
   os.system('mkdir -p %s/autogen' % (staticDir, ))

   execWithVirtEnv('mkvirtualenv %s' % (projectName, ))

   pipPackages = projectSettings['PipPackages'].split(',')
   for pipPkg in pipPackages:
      execWithVirtEnv('workon %s; pip install %s' % (projectName, pipPkg))

   #shellutils.expand_link('misc/examples_project')
   examplesDir = kosandDir + '/misc/example_project/'
   os.system('cp %s/index.jsx %s' % (examplesDir, jsxDir))
   os.system('cp %s/serv.py %s' % (examplesDir, pyDir))
   os.system('cp %s/index.scss %s' % (examplesDir, sassDir))
   os.system('cp %s/index.html %s' % (examplesDir, templatesDir))

