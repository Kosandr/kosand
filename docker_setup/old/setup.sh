#!/bin/bash

apt install nginx-extras

pip3 install gunicorn Flask libsass sh
pip3 install user_agents

mkdir -p ../static-nginx/autogen

mkdir -p /sec/{nginx_confs,logs}
