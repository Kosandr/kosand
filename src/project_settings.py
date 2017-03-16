
import configparser, argparse

default_conf_path = '.kosand.conf'

import utiltools
from utiltools import shellutils

def gen_default_conf(projectName='None'):
   '''Generates default project settings'''

   ret = {
      'ProjectSettings' : {
         'ProjectName' : projectName,
         'JsxDir' : 'src/jsx',
         'PyDir' : 'src/py',
         'GuniPyApp' : 'serv:app',
         'SassDir' : 'src/sass',
         'TemplatesDir' : 'src/templates',
         'StaticDir' : 'static-nginx',
         'StaticUrl' : 'None',
         'ProjectDomain' : 'None',
         'ProjectUrl' : 'None',
         'IP' : 'localhost',
         'Port' : '4001',
         'NumWorkers' : 'None',
         'SslEnabled' : 'None',
         'SslDir' : 'None',
         'SslPub' : 'None', #fullchain.pem
         'SslPriv' : 'None', #privkey.pem
         'AdminEmailNotifications' : 'None',
         'PipPackages' : 'flask,flask-session,user_agents',
         'NpmPackages' : 'None'
         #TODO: local npm and pip packages
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
      'JsxDir', 'PyDir', 'GuniPyApp', 'SassDir', 'TemplatesDir',
      'IP', 'StaticDir', 'Port', 'NumWorkers', 'ProjectName',
      'ProjectDomain', 'NpmPackages', 'PipPackages',
      'SslEnabled', 'SslDir', 'SslPub', 'SslPriv'
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
         #print('section:', section, ' field:', field, ' val:', field_val)
         config.set(section, field, field_val)

   with open(conf_path, 'w') as conf_file:
      config.write(conf_file)

   return config


