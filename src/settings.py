
import configparser, argparse

default_conf_path = '.kosand.conf'

import utiltools
#from utiltools import shellutils
find_file_recursive_parent = utiltools.shellutils.find_file_recursive_parent

def gen_default_conf(projectName='None'):
   '''Generates default project settings'''

   ret = {
      'ProjectSettings' : {
         'ProjectName' : projectName,
         'JsxDir' : 'src/jsx',
         'PyDir' : 'src/py',
         'SassDir' : 'src/sass',
         'TemplatesDir' : 'src/templates',
         'StaticDir' : 'static-nginx',
         'StaticUrl' : 'None',
         'ProjectDomain' : 'None',
         'ProjectUrl' : 'None',
         'IP' : 'localhost',
         'Port' : '4001',
         'NumWorkers' : 'None',
         'SslPub' : 'None',
         'SslPriv' : 'None',
         'AdminEmailNotifications' : 'None'
      },
      'DevSettings' : {},
      'ProductionSettings' : {}
   }

   return ret

def get_conf_section_list():
   return ['ProjectSettings', 'DevSettings', 'ProductionSettings']

def get_conf_section_field_list(sectionName):
   '''Returns field names in each config section'''

   psFields = [
      'JsxDir', 'PyDir', 'SassDir', 'TemplatesDir', 'IP', 'StaticDir',
      'Port', 'NumWorkers', 'ProjectName', 'SslPub', 'SslPriv'
   ]
   devFields = []
   prodFields = []

   if sectionName == 'ProjectSettings':
      return psFields
   elif sectionName == 'DevSettings':
      return devFields
   elif sectionName == 'ProductionSettings':
      return prodFields
   return []

def gen_new_conf(project_name, user_arg_conf={}, conf_path=default_conf_path):
   '''Writes default configuration to conf_path If no user settings,
      then uses settings from gen_default_conf()

      user_arg_conf = user-supplied default settings
   '''

   sections = get_conf_section_list()
   default_conf = gen_default_conf(project_name)

   config = configparser.ConfigParser()

   for i, section in enumerate(sections):
      config.add_section(section)
      fields = get_conf_section_field_list(section)

      userDefaults = user_arg_conf.get(section, {})
      autoDefaults = default_conf[section]

      for field in fields:
         field_val = userDefaults.get(field, autoDefaults[field]) #autoDefaults.get(field, 'None'))
         print('section:', section, ' field:', field, ' val:', field_val)
         config.set(section, field, field_val)

   with open(conf_path, 'w') as conf_file:
      config.write(conf_file)

   return config

def parse_conf(conf_path):
   '''Takes configuration path, and returns dictionary of settings'''

   settings = configparser.ConfigParser()
   settings.read(conf_path)
   ret = get_conf_data(settings)
   #print(ret)
   #print(conf.sections())
   return ret

def get_conf_data(conf):
   '''Given configpraser, returns data as dictionary'''

   #defaultConf = gen_default_conf()
   ret = {}

   for section in get_conf_section_list():
      #sectDefaults = defaultConf[section]
      sectFields = get_conf_section_field_list(section)
      ret[section] = {}

      for fieldName in sectFields:
         fieldVal = conf.get(section, fieldName)
         if fieldVal == 'None':
            fieldVal = None
         ret[section][fieldName] = fieldVal

   return ret



def gen_arg_parser():

   init_help = '''main actions:
      install           (global) install the global kosand project
      init <project-name>
                        new project
      setup             (project) run after cloning to setup
      rm [-p <project-name>]
                        remove current project from the list
      watch [-p <project-name>]
                        watch project live
      start [-p <project-name>]
                        start running project
      stop [-p <project-name>]
                        stop running project
      status [-p <project-name>]
                        (local) print current status
      status --global   (global) status of all projects
   '''

   p = parser = argparse.ArgumentParser(
         'kosand', epilog=init_help,
         formatter_class=argparse.RawTextHelpFormatter)

   p_help_str = 'name of new project (use with init only)'
   g_help_str = 'run command in global mode (used with status)'

   p.add_argument('-p', '--project-name', nargs='?', help=p_help_str)
   p.add_argument('-g', '--global', help=g_help_str)
   p.add_argument('-m', '--mode', nargs='?', help='mode: devel/prod')

   choices = ['install', 'init', 'setup', 'rm', 'watch', 'start', 'stop', 'status']
   p.add_argument('action', nargs='?', choices=choices)

   return parser


