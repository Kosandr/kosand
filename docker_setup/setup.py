#!/usr/bin/python3

from utiltools import shellutils as shu
import os, sh


run_bash = shu.run_bash



def install_docker():
   def add_docker_repo():
      cmd = '''
      sudo apt-get update;
      sudo apt-get install \
          apt-transport-https \
          ca-certificates \
          curl \
          software-properties-common;
      curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
      sudo apt-key fingerprint 0EBFCD88;

      sudo add-apt-repository \
         "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
         $(lsb_release -cs) \
         stable"
      '''
      return run_bash(cmd, get_out=False)

   def install():
      cmd = '''
         sudo apt-get update; sudo apt-get install docker-ce
      '''
      return run_bash(cmd, get_out=False)

   add_docker_repo()
   install()

   pass

def is_docker_installed():
   try:
      sh.docker()
   except Exception as e:
      return False
   return True

def check_and_install_docker():
   have_docker = is_docker_installed()
   if not have_docker:
      install_docker()

   print('have docker:', have_docker)


'''def docker_build(path):

   import pexpect
   child = pexpect.spawn()'''


def write_img_buildid(name):
   sh.shellu('set', 'kosan_bfske_latest_docker_img_build_id', name)
   #pass

def get_img_buildid():
   return str(sh.shellu('get', 'kosan_bfske_latest_docker_img_build_id')).strip()


def main():
   check_and_install_docker()

   build_flags = '--no-cache'
   build_flags = '' #comment this line to re-build from scratch

   cmd = 'docker build %s -f dock/Dockerfile dock' % (build_flags,)

   hide_out = True #set to false to look at output as it goes
   ret = run_bash(cmd, hide_out)

   print(ret)

   splitted = ret.split('Successfully built ')

   if len(splitted) is not 2:
      print('failed building image:', ret)
   else:
      build_id = splitted[1]
      #build_id = 'a6072e47be06'
      write_img_buildid(build_id)
      print('running image: %s' % (build_id,))

      run_bash('docker run -t -i %s /bin/bash' % (build_id,), False)


def run(build_id, shared_drive_path, cmd):
   volume_args = '-v %s:/sec' % (shared_drive_path,)

   ports_args = '-p 4247:4247'
   full_cmd = 'docker run -t -i %s %s %s %s' % (volume_args, ports_args, build_id, cmd)

   run_bash(full_cmd, False)

   #pass

if __name__ == '__main__':
   main()



def install_deps():

   def base_deps():
      cmd = '''
         sudo apt -y install sqlite3
         sudo pip3 install Flask gunicorn user_agents
      '''
      run_bash(cmd, get_out=False)

   def flask_session_deps():
      cmd = '''
         sudo apt -y install redis-server
         pip3 install redis Flask-Session
      '''
      run_bash(cmd, get_out=False)

   base_deps()
   flask_session_deps()




