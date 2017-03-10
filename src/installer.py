import os, sys
from utiltools import shellutils


sh_get_path = shellutils.get_abs_path_relative_to

def self_install(mode):
   warning_str = 'Warning: this will overwrite /sec. Proceed? (yes/no)'
   proceed_str = input(warning_str)
   if proceed_str == 'yes':
      print('installing...')
   else:
      print('exiting...')
      sys.exit(1)

   #shellutils.cwd()
   kosand_dir = sh_get_path(os.path.realpath(__file__), '..')
   kosand_path = kosand_dir + '/kosand'

   os.system('sudo ln -s %s /usr/bin/kosand' % (kosand_path,))

   install_dir = '%s/misc/install_dir/sec' % (kosand_dir,)
   #os.system('sudo cp %s /' % (install_dir, ))
   os.system('sudo rsync -a %s /' % (install_dir, ))


   is_prod = 0
   if mode == 'devel':
      is_prod = 0
   elif mode == 'prod':
      is_prod = 1

   os.system('sudo echo %s >/sec/is_prod' % (is_prod))

   os.system('sudo apt update && sudo apt upgrade')

   #mariadb
   needed_packages = ['gunicorn', 'nginx-extras']
   for package_name in needed_packages:
      os.system('sudo apt install ' + package_name)




