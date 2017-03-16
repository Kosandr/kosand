import os, sys
from utiltools import shellutils

sh_get_path = shellutils.get_abs_path_relative_to

def install_kosand_packages():
   os.system('sudo apt update && sudo apt upgrade')

   #gunicorn = installed with pip
   #mariadb
   needed_packages = [
      'nginx-extras', 'python3', 'python3-pip'
   ]
   for pkg_name in needed_packages:
      os.system('sudo apt install ' + pkg_name)

   pip_packages = ['virtualenv', 'virtualenvwrapper', 'pyparsing']
   for pkg_name in pip_packages:
      os.system('pip install ' + pkg_name)

   #if breaks, see this thread:
   #http://stackoverflow.com/questions/19549824/terminal-issue-with-virtualenvwrapper-after-mavericks-upgrade
   os.system('echo "source `which virtualenvwrapper.sh`" >>~/.bashrc')

   pass

from os.path import join

NGINX_CONF_PATH = '/etc/nginx/'
NGINX_CONF_PATH = '%s/nginx.conf' % (NGINX_CONF_PATH,)
KOSANDR_ORG_URL_HTTPS = 'https://github.com/Kosandr' #CAREFUL WITH SLASHES
KOSANDR_ORG_URL_SSH = 'git@github.com:Kosandr' #CAREFUL WITH SLASHES

KOSAND_DATA_DIR = '/sec/'
KOSAND_BACKUP_DIR = '%sbackups/' % (KOSAND_DATA_DIR, )

KOSAND_NGINX_INCLUDE_PATH = '%sinternal/nginx-confs/' % (KOSAND_DATA_DIR, )
#AS SEEN IN nginx.conf
KOSAND_INCLUDE_PATH_FOR_NGINX_CONF = KOSAND_NGINX_INCLUDE_PATH + '*'

#TODO: make pip install a separate function, and install pyparsing here??
def setup_nginx_parser():
   cmd = 'cd /tmp; git clone %s/nginxparser.git; cd nginxparser; sudo python3 setup.py install; cd ..; sudo rm -R nginxparser' % (KOSANDR_ORG_URL_HTTPS, )
   os.system(cmd)

def backup_nginx_conf():
   install_backups_path = KOSAND_BACKUP_DIR + '/install/'
   nginx_backups_path = install_backups_path + '/nginx_confs/'
   from utiltools.shellutils import ls
   existing_backup_names = ls(nginx_backups_path)

   existing_backup_nums = list(map(lambda x: int(x), existing_backup_names))

   curr_backup_ver = 0
   if len(existing_backup_nums) > 0:
      curr_backup_ver = max(existing_backup_nums) + 1

   full_backup_path = nginx_backups_path + str(curr_backup_ver)
   os.system('cp %s %s' % (NGINX_CONF_PATH, full_backup_path))


def link_nginx_confs():
   import nginxparser
   nginx_conf = nginxparser.load(open(NGINX_CONF_PATH))
   needed_section = None

   def find_sect(sect, name):
      for sub_sect in sect:
         if len(sub_sect) > 0 and len(sub_sect[0]) > 0 and sub_sect[0][0] == name:
            return sub_sect
      return None

   http_sect = find_sect(nginx_conf, 'http')[1]
   #if http_sect is not None:
   #   server_sect = find_sect(http_sect, 'server')

   #for section in nginx_conf:
   #   if len(section) > 0 and len(sect[0] > 0) and sect[0][0] == 'http':
   #      needed_section = section

   #find include
   includes = []
   for field in http_sect:
      if type(field) is list and (len(field) == 2) and type(field[0]) is str:
         if field[0] == 'include':
            includes.append(field)

   already_included = False
   for include in includes:
      if include[1] == KOSAND_INCLUDE_PATH_FOR_NGINX_CONF:
         already_included = True

   if not already_included:
      http_sect.append(['include', KOSAND_INCLUDE_PATH_FOR_NGINX_CONF])

      backup_nginx_conf()

      tmp_nginx_path = '/tmp/kosand_nginx.conf'
      with open(tmp_nginx_path, 'w') as f:
         f.write(nginxparser.dumps(nginx_conf) + '\n')
      arg_tuple = (tmp_nginx_path, NGINX_CONF_PATH, tmp_nginx_path)
      os.system('sudo cp %s %s; rm %s' % arg_tuple)
   else:
      print('NEEDED NGINX CONF FIELD ALREADY FOUND!')


def self_install(mode):
   warning_str = 'Warning: this will overwrite /sec. Proceed? (yes/no) '
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

   install_kosand_packages()

   setup_nginx_parser()
   link_nginx_confs()


