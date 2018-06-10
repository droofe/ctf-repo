#!/usr/bin/env python2

import os
import struct
from time import sleep
from pwn import *

context.terminal = 'tmux splitw -h'.split()

# CHANGE THESE
exe = context.binary = ELF('./babyheap')
libc = ELF('./libc.so.6')

gdbscript = """
continue
""".format(**locals())

def start(argv=[], *a, **kw):
	if args.GDB:
		io = gdb.debug([exe.path] + argv, env={"LD_LIBRARY_PATH":"."}, gdbscript=gdbscript, *a, **kw)
	elif args.REMOTE:
		# AND THIS
		io = remote("honj.in", 4024)
	else:
		io = process([exe.path] + argv, env={"LD_LIBRARY_PATH":"."}, *a, **kw)
	return io

s = start()

s.interactive()
