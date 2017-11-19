#!/usr/bin/python3

import sys
import setup

from utiltools import shellutils as shutil

img_build_id = setup.get_img_buildid()

shared_drive_path = shutil.get_abs_path_relative_to('./dock') + '/dock'
#print(shared_drive_path)

if len(sys.argv) == 2:
   shared_drive_path = sys.argv[1]


#run_cmd = '/root/orgs/Kosandr/base-flask-skeleton/pull-and-run.sh'
run_cmd = '/bin/bash'

print('running app with shared drive:', shared_drive_path)

setup.run1(img_build_id, shared_drive_path, run_cmd)


