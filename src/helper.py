
#GLOBALS
NGINX_CONF_PATH = '/etc/nginx/'
NGINX_CONF_PATH = '%s/nginx.conf' % (NGINX_CONF_PATH,)
KOSANDR_ORG_URL_HTTPS = 'https://github.com/Kosandr' #CAREFUL WITH SLASHES
KOSANDR_ORG_URL_SSH = 'git@github.com:Kosandr' #CAREFUL WITH SLASHES

KOSAND_DATA_DIR = '/sec/'
KOSAND_BACKUP_DIR = '%sbackups/' % (KOSAND_DATA_DIR, )

KOSAND_NGINX_INCLUDE_PATH = '%sinternal/nginx-confs/' % (KOSAND_DATA_DIR, )
#AS SEEN IN nginx.conf
KOSAND_INCLUDE_PATH_FOR_NGINX_CONF = KOSAND_NGINX_INCLUDE_PATH + '*'


import configparser

import utiltools
from utiltools import shellutils

def parse_conf(conf_path, get_conf_section_list, get_conf_section_fields):
   '''Takes configuration path, and returns dictionary of settings'''

   settings = configparser.ConfigParser()
   settings.read(conf_path)
   ret = get_conf_data(settings, get_conf_section_list, get_conf_section_fields)
   #print(ret)
   #print(conf.sections())
   return ret

def get_conf_data(conf, get_conf_section_list, get_conf_section_field_list):
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



def gen_new_conf(conf_path, gen_default_conf,
                 get_conf_section_list, get_conf_section_field_list,
                 user_arg_conf={}, project_name=None):
   '''Writes default configuration to conf_path.
      If no default user settings, then uses
      settings from gen_default_conf()

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


find_conf_path = utiltools.shellutils.find_file_recursive_parent

def find_conf(conf_name):
   return find_conf_path(conf_name)

def get_kosand_conf():
   from global_settings import default_conf_path, get_conf_section_list, get_conf_section_field_list
   return parse_conf(default_conf_path, get_conf_section_list, get_conf_section_field_list)

def update_kosand_conf(kConf):
   pass



