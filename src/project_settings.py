
import configparser, argparse
import helper

import utiltools
from utiltools import shellutils

#projectName gets ignored
def gen_default_conf(projectName='None', domain=None, url=None):
   '''Generates default project settings'''

   if domain is None:
      domain = 'None'
   if url is None:
      url = 'None'

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
         'ProjectDomain' : domain,
         'ProjectUrl' : url, #path after domain
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


default_conf_path = '.kosand.conf'
def gen_new_conf(project_name, user_arg_conf={}, conf_path=default_conf_path):
   return helper.gen_new_conf(conf_path, gen_default_conf, get_conf_section_list, get_conf_section_field_list, user_arg_conf, project_name)


