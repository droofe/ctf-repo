#!/bin/bash

cd /opt/ctf/fantasticiot/rw

if [[ "i386" == "x86_64" ]] || [[ "x86_64" == "x86_64" ]] ; then
  ../ro/fantasticiot 2>/dev/null
else
  qemu-x86_64 ../ro/fantasticiot 2>/dev/null
fi