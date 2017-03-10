
import settings, os

def new_project(projectName):
   config_raw = settings.gen_new_conf(projectName)

   config = settings.get_conf_data(config_raw)
   print(config)

   project_settings = config['ProjectSettings']

   jsx_dir = project_settings['JsxDir']
   py_dir = project_settings['PyDir']
   sass_dir = project_settings['SassDir']
   templates_dir = project_settings['TemplatesDir']
   static_dir = project_settings['StaticDir']

   os.system('mkdir -p ' + jsx_dir)
   os.system('mkdir -p ' + py_dir)
   os.system('mkdir -p ' + sass_dir)
   os.system('mkdir -p ' + templates_dir)
   os.system('mkdir -p ' + static_dir)



