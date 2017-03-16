import os, project_settings, helper
from utiltools import shellutils

sh_get_path = shellutils.get_abs_path_relative_to
kosandDir = sh_get_path(os.path.realpath(__file__), '..')

def execWithVirtEnv(cmd):
   sourceVirtEnv = 'source `which virtualenvwrapper.sh`; '
   os.system('bash -c "%s %s"' % (sourceVirtEnv, cmd))


def generate_nginx_conf(conf):
   ps = conf['ProjectSettings']

   ssl_str = ''
   if ps['SslEnabled'] == True:
      ssl_dir = ps['SsslDir'] + '/'
      ssl_pub = ssl_dir + ps['SslPub']
      ssl_priv = ssl_dir + ps['SslPriv']

      ssl_str = '''
         ssl_certificate %s;
         ssl_certificate_key %s;
      ''' % (ssl_pub, ssl_priv)

   placeholder_str = '''server {
      server_name %s www.%s;

      %s


   }''' % (ps['ProjectDomain'], ps['ProjectDomain'], ssl_str)
   pass

def new_project(projectName):
   config_raw = project_settings.gen_new_conf(projectName)

   config = helper.get_conf_data(config_raw, project_settings.get_conf_section_list())
   #print(config)

   projectSettings = config['ProjectSettings']

   jsxDir = projectSettings['JsxDir']
   pyDir = projectSettings['PyDir']
   sassDir = projectSettings['SassDir']
   templatesDir = projectSettings['TemplatesDir']
   staticDir = projectSettings['StaticDir']

   for dir_path in [jsxDir, pyDir, sassDir, templatesDir, staticDir]:
      os.system('mkdir -p ' + dir_path)
   os.system('mkdir -p %s/autogen' % (staticDir, ))

   execWithVirtEnv('mkvirtualenv %s' % (projectName, ))

   pipPackages = projectSettings['PipPackages'].split(',')
   for pipPkg in pipPackages:
      execWithVirtEnv('workon %s; pip install %s' % (projectName, pipPkg))

   #shellutils.expand_link('misc/examples_project')
   examplesDir = kosandDir + '/misc/example_project/'
   os.system('cp %s/index.jsx %s' % (examplesDir, jsxDir))
   os.system('cp %s/serv.py %s' % (examplesDir, pyDir))
   os.system('cp %s/index.scss %s' % (examplesDir, sassDir))
   os.system('cp %s/index.html %s' % (examplesDir, templatesDir))

   generate_nginx_conf(config)


