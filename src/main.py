#!/usr/bin/env python3

from settings import gen_arg_parser
from installer import self_install

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

      self_install(mode)

   print(args)



print(main())
