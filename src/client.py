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

class Config:
   def __init__(self, install_path=None, config_path=None):

      #guess
      if install_path is None and config_path is None:
         install_path, config_path = self.guess_config_location()

      #we got config file, but idk where nstall_path is
      elif config_path is not None and install_path is None:
         pass

      #we have install_path (which has symlink to config_path)
      elif install_path is not None:
         sh_read_file(install_path + '/' + 'kosandr.conf')

   def init_with_pathes(self):

   def guess_config_location(self):
      self.install_path = DEFAULT_INSTALL_PATH
      self.config_path = DEFAULT_CONFIG_PATH
      self.init_with_pathes()
      return install_path, config_path

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

