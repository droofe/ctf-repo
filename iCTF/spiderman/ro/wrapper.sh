#!/bin/bash

cd /opt/ctf/spiderman/rw

if [[ "i386" == "x86_64" ]] || [[ "x86_64" == "x86_64" ]] ; then
  ../ro/spiderman 2>/dev/null
else
  qemu-x86_64 ../ro/spiderman 2>/dev/null
fi