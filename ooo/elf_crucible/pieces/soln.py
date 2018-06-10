from pwn import *
from sys import argv

def io():
    if "remote" in argv:
        s = remote("e4771e24.quals2018.oooverflow.io", 31337);
    elif
