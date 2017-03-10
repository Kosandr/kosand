
import configparser, argparse

default_conf_path = '.kosand.conf'

import utiltools
#from utiltools import shellutils
find_file_recursive_parent = utiltools.shellutils.find_file_recursive_parent

def gen_default_conf():
   '''Generates default project settings'''

   ret = {
      'ProjectSettings' : {
         'JsxDir' : 'src/jsx',
         'PyDir' : 'src/py',
         'SassDir' : 'src/sass',
         'TemplatesDir' : 'src/templates',
         'StaticDir' : 'static-nginx',
         'StaticUrl' : None,
         'ProjectDomain' : None,
         'ProjectUrl' : None,
         'IP' : 'localhost',
         'Port' : 4001,
         'NumWorkers' : None,
         'ProjectName' : None,
         'SslPub' : None,
         'SslPriv' : None,
         'AdminEmailNotifications' : None
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
      'JsxDir', 'PyDir', 'SassDir', 'TemplatesDir', 'IP',
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

def gen_new_conf(user_arg_conf={}, conf_path=default_conf_path):
   '''Writes default configuration to conf_path If no user settings,
      then uses settings from gen_default_conf()

      user_arg_conf = user-supplied default settings
   '''

   sections = get_conf_section_list()
   default_conf = gen_default_conf()

   config = configparser.ConfigParser()

   for i, section in enumerate(sections):
      config.add_section(section)
      fields = get_conf_section_field_list(section)

      userDefaults = user_arg_conf.get(section, {})
      autoDefaults = default_conf[section]

      for field in fields:
         field_val = userDefaults.get(field, autoDefaults[field])
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
         ret[section][fieldName] = conf.get(section, fieldName)

   return ret



def gen_arg_parser():

   init_help = '''main actions:
      init              (global) init new project
      setup             (project) run after cloning to setup assets, etc
      update            (project) copies files and runs project
      run               (
      stop
      status            (global/local) print current status of project
      install           (global) install the global kosand project
   '''

   p = parser = argparse.ArgumentParser(
         'kosand', epilog=init_help,
         formatter_class=argparse.RawTextHelpFormatter)

   p.add_argument('-p', '--project-name', nargs='?', help='name of new project (use with init only)')
   p.add_argument('-l', '--local', help='run command in local mode')

   #p.add_argument('-d', '--debug', help='debug mode (use with run only)')
   #p.add_argument('-r', '--release', help='release mode (use with run only)')
   p.add_argument('-m', '--mode', nargs='?', help='mode: devel/prod')

   choices=['init', 'setup', 'update', 'run', 'stop', 'status', 'install']
   p.add_argument('action', nargs='?', choices=choices)

   return parser


