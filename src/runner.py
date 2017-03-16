import os
import helper

def watch_site(project_name=None):
   pass

def run_site(project_name=None):
   conf_path, conf = get_conf()
   print(conf_path, '\n', conf)
   os.system('pywatch --help')

   ps = conf['ProjectSettings']

   python_path = ps['PyDir']

   run_cmd = 'gunicorn --pythonpath %s %s'
   #os.system('gunicorn --pythonpath '

def stop_site(project_name=None):
   pass

def get_conf():
   conf_path = helper.find_conf('.kosand.conf')
   if conf_path is None:
      print("couldn't find .kosand.conf")
      sys.exit(1)
   conf = settings.parse_conf(conf_path)
   return (conf_path, conf)


