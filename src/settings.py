
import configparser

default_conf_path = '.kosand.conf'

from utiltools.shellutils import find_file_recursive_parent

def gen_default_conf():
   ret = {
      'ProjectSettings' : {
         'JsxDir' : 'src/jsx',
         'PyDir' : 'src/py',
         'SassDir' : 'src/sass',
         'TemplatesDir' : 'src/templates',
         'IP' : 'localhost',
         'Port' : 4001,
         'NumWorkers' : None,
         'ProjectName' : None,
         'SslPub' : None,
         'SslPriv' : None,
         'AdminEmailNotifications', None,
      },
      'DevSettings' : {
      },
      'ProductionSettings' : {

      }
   }

   return ret

#project_name
def gen_new_conf(user_arg_conf={}, conf_path=default_conf_path):

   default_conf = gen_default_conf()

   config = configparser.ConfigParser()
   config.add_section('ProjectSettings')
   config.add_section('DevSettings')
   config.add_section('ProductionSettings')

   psFields = [
      'JsxDir', 'PyDir', 'SassDir', 'TemplatesDir', 'IP',
      'Port', 'NumWorkers', 'ProjectName', 'SslPub', 'SslPriv'
   ]
   psUserDefaults = user_arg_conf.get('ProjectSettings', {})
   psDefaults = default_conf['ProjectSettings']

   for field in psFields:
      field_val = user_arg_conf.get(field, psDefaults[field])
      config.set('ProjectSettings', field, field_val)

   devFields = []
   devDefaults = default_conf['DevSettings']
   devUserDefaults = user_arg_conf.get('DevSettings', {})
   for field in devFields:
      field_val = devUserDefaults.get(field, devDefaults[field])
      config.set('DevSettings', field, field_val)


   prodFields = []
   prodDefaults = default_conf['ProductionSettings']
   prodUserDefaults = user_arg_conf.get('ProductionSettings', {})
   for field in prodFields:
      field_val = prodUserDefaults.get('ProductionSettings', {})
      conf.set('ProductionSettings', field, field_val)

   with open(conf_path, 'w') as conf_file:
      config.write(conf_file)

   return config

def parse_conf(conf_path):
   settings = configparser.ConfigParser()
   settings.read(conf_path)
   ret = get_conf_data(settings)
   #print(ret)
   #print(conf.sections())
   return ret

def get_conf_data(conf):
   ret = {}
   sects = ['ProjectSettings', 'DevSettings', 'ProductionSettings']
   for section in sects:
      ret[section] = conf.get(section, blah)





