
import settings, os

def new_project(projectName):
   config_raw = settings.gen_new_conf(projectName)

   config = settings.get_conf_data(config_raw)
   #print(config)

   project_settings = config['ProjectSettings']

   projectName = project_settings['ProjectName']

   jsx_dir = project_settings['JsxDir']
   py_dir = project_settings['PyDir']
   sass_dir = project_settings['SassDir']
   templates_dir = project_settings['TemplatesDir']
   static_dir = project_settings['StaticDir']

   os.system('mkdir -p ' + project_settings['JsxDir'])
   os.system('mkdir -p ' + project_settings['PyDir'])
   os.system('mkdir -p ' + project_settings['SassDir'])
   os.system('mkdir -p ' + project_settings['TemplatesDir'])
   os.system('mkdir -p ' + project_settings['StaticDir'])


   def execWithVirtEnv(cmd):
      sourceVirtEnv = 'source `which virtualenvwrapper.sh`; '
      os.system('bash -c "%s %s"' % (sourceVirtEnv, cmd))

   execWithVirtEnv('mkvirtualenv %s' % (projectName, ))
   #os.system('bash -c "%s mkvirtualenv %s"' % (sourceVirtEnv, projectName))

   examples_dir = 'misc/example_project'
   #os.system('cp



