#!/bin/bash

cd /opt/ctf/shelter/rw

if [[ "i386" == "i386" ]] || [[ "x86_64" == "i386" ]] ; then
  ../ro/shelter 2>/dev/null
else
  qemu-i386 ../ro/shelter 2>/dev/null
fi