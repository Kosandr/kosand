#!/usr/bin/env python3
DEFAULT_CONFIG_PATH = '/etc/kosandr.conf'
DEFAULT_INSTALL_PATH = '/opt/kosandr'

from IPC.icloakipc import IPCClient
from IPC.shellutils import file_exists as sh_file_exists, read_file as sh_read_file
from sh import mkdir as sh_mkdir

import time


#utils file

#config file path to dictionary
def get_conf_from_path(path):
   return {}

#main file

####TODO:
'''
obtain lock to make sure only 1 instance is running
create lib library and correct infrastructure

change prompt:
http://stackoverflow.com/questions/7120426/invoke-bash-run-commands-inside-new-shell-then-give-control-back-to-user
'''
#os.system('''bash --rcfile <(echo '. ~/.bashrc; export PS1="test"') ''')
#os.system("bash -c 'bash --rcfile <(echo \". ~/.bashrc; export PS1=test\") ' ")

'''
#bad bash -c "export PS1='hiii'; bash"
#bad os.system(' bash -c "export PS1=\'hiii\'; bash"  ')

''' ####end TODO

def error(x):
   raise x

class Config:
   def __init__(self, install_path=None, config_path=None):

      #we have install_path (which has symlink to config_path)
      if install_path is not None and config_path is None:
         self.init_with_install_path(install_path)
         #sh_read_file(install_path + '/' + 'kosandr.conf')

      #we got config file, but idk where install_path is
      elif config_path is not None:
         self.init_with_config_path(config_path)

      #guess
      elif install_path is None and config_path is None:
         self.init_guess_config_location()

      #same as "elif install_path != None && config_path != None:"
      else:
         err_msg = 'specify either install_path or config_path but not both'
         error(err_msg)



   def init_with_both_pathes(self):
      pass

   def init_with_config_path(self):
      pass

   def init_guess_config_location(self):
      self.install_path = DEFAULT_INSTALL_PATH
      self.config_path = DEFAULT_CONFIG_PATH
      self.init_with_both_pathes()

   def self_install(self):
      mkdir('/tmp/ha')

class Kosandr:
   def __init__(self, install_path=None, config_path=None):
      self.conf = Config(install_path, config_path)

   def init_ipc_client(address='/tmp/ipc_example.sock',
                       namespace='test',
                       sync=True):
      client = IPCClient.new_unix_transport(
         address=address,
         namespace=namespace,
         sync=sync)
      client.ipc_connect()
      return client


   def init_client():
      is_installed = False
      if sh_file_exists('/opt/kosandr'):
         is_installed = True

      print(is_installed)
      self.client = init_ipc_client()


kosandr = Kosandr()

while 1:
   print(client.get_string())
   time.sleep(5)

