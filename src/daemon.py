from time import sleep
from daemonize import Daemonize

#import sys
#sys.path.append('IPC')
from IPC.icloakipc import IPCServer, exposed, ExposedAPI


class API(ExposedAPI):
   def __init__(self, session, server):
      super(API, self).__init__("test", session, server)
      self.counter = 0

   @exposed
   def set_prompt():
      pass

   @exposed
   def new_app():
      pass

   @exposed
   def new_site():
      pass


   @exposed
   def get_string(self):
      self.counter += 1
      return "I am a string! %s" % self.counter


def main():
   perms=None
   address = '/tmp/ipc_example.sock'
   print("ADDRESS: %s" % address)
   srv = IPCServer.new_unix_transport(address, API, permissions=perms)
   srv.start()


####
#def main():
#   time.sleep(5)
main()

sys.exit(1)
pid = "/tmp/test.pid"
daemon = Daemonize(app="test_app", pid=pid, action=main)
daemon.start()



