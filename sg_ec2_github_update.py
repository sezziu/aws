#!/usr/bin/env python

import requests
import os

username = '<github_usernamexxxx'
token = '<tokenidxxxxx>'

data = requests.get('https://api.github.com/meta', auth=(username, token))

hooks = data.json()['hooks']
git = data.json()['git']
pages = data.json()['pages']
#importer = data.json()['importer']
dataload = hooks + git + pages
security_group = "sg-xxxxxx"

for i in dataload:
    os.system("aws ec2 authorize-security-group-ingress --group-id " + security_group + " --protocol tcp --port 80 --cidr " + i)
    print i + " port:80 added!"
    os.system("aws ec2 authorize-security-group-ingress --group-id " + security_group + " --protocol tcp --port 443 --cidr " + i)
    print i + " port:443 added!"
