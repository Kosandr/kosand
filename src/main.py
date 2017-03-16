#!/usr/bin/env python3

import sys
from helper import gen_arg_parser
from installer import self_install
from project_manager import new_project
import runner

def main():
   arg_parser = gen_arg_parser()
   args = arg_parser.parse_args()

   action = args.action

   if action is None:
      arg_parser.print_help()
   if action == 'install':
      #is_prod
      mode = args.mode
      if args.mode not in ['devel', 'prod']:
         print('setup needs -m devel/prod')
         sys.exit(1)
      self_install(mode)
   elif action == 'init':
      if args.project_name == None:
         print('new project requires a name')
         sys.exit(1)

      new_project(args.project_name)
   elif action == 'start':
      runner.run_site(args.project_name)

   print(args)


print(main())

