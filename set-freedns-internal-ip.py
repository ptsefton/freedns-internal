#!/usr/bin/env python3
import os
import socket
import json
import socket
from urllib.request import urlopen

dir = os.path.dirname(__file__)
secret_path = os.path.join(dir, '.freedns_secret')
ip_path = os.path.join(dir, '.ip')

secret = json.load(open(secret_path, 'r'))['secret']
url = 'https://freedns.afraid.org/dynamic/update.php?%s&address=%s'

f = open(ip_path, 'a').close()
f = open(ip_path, 'r')
oldip = f.read()
f.close()

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('gmail.com', 80))
ip = s.getsockname()[0]

open(ip_path, 'w').write(ip)
if ip != oldip:
     new_url = url % (secret, ip)
     urlopen(new_url).read()

