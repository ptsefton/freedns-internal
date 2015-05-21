#!/usr/bin/env python3
import os
import socket
import json
import socket
import os
from urllib.request import urlopen

secret = json.load(open(".freedns_secret","r"))['secret']
url = "https://freedns.afraid.org/dynamic/update.php?%s&address=%s" 





f = open(".ip", 'a').close()
f = open(".ip",'r')
oldip = f.read()
f.close()


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("gmail.com",80))
ip = s.getsockname()[0]

open(".ip","w").write(ip)
if ip != oldip:
     new_url = url % (secret, ip)
     urlopen(new_url).read()

