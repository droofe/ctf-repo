#!/bin/bash

cd /opt/ctf/venom/rw

if [[ "i386" == "x86_64" ]] || [[ "x86_64" == "x86_64" ]] ; then
  ../ro/venom 2>/dev/null
else
  qemu-x86_64 ../ro/venom 2>/dev/null
fi