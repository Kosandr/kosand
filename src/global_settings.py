import helper

import configparser, argparse

import utiltools
from utiltools import shellutils

def gen_default_conf(projectName='None'):
   '''Generates default Kosand settings'''

   ret = {
      'KosandSettings' : {
         'DataDir' : '/sec',
         'PortRange' : '4000-5000',
         'TakenPorts' : 'None',
         'Projects' : 'None',
         'ProjectPaths' : 'None',
         'AptPackages' : 'nginx-extras,python3,python3-pip', #gunicorn = install through pip, mariadb
         'PipPackages' : 'virtualenv,virtualenvwrapper,pyparsing',
      },
      'DefaultProjectSettings' : { #TODO: USE THIS IN PROJECT SETTINGS
         'NumWorkers' : 'None',
         'AdminEmailNotifications' : 'None',
         'PipPackages' : 'flask,flask-session,user_agents',
         'NpmPackages' : 'None'
      }
   }

   return ret

def get_conf_section_list():
   return ['KosandSettings', 'DefaultProjectSettings']

def get_conf_section_field_list(sectionName):
   '''Returns field names in each config section'''

   ksFields = [
      'DataDir', 'PortRange', 'TakenPorts', 'Projects',
      'ProjectPaths', 'AptPackages', 'PipPackages'
   ]
   dpsFields = [
      'NumWorkers', 'AdminEmailNotifications',
      'PipPackages', 'NpmPackages'
   ]

   if sectionName == 'KosandSettings':
      return ksFields
   elif sectionName == 'DefaultProjectSettings':
      return dpsFields
   return []

default_conf_path = '/sec/internal/kosand.conf'
def gen_new_conf(conf_path=default_conf_path, user_arg_conf={}):

   return helper.gen_new_conf(conf_path, gen_default_conf, get_conf_section_list, get_conf_section_field_list, user_arg_conf, None)


