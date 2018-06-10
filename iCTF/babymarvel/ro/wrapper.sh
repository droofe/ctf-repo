#!/bin/bash

cd /opt/ctf/babymarvel/rw

if [[ "i386" == "x86_64" ]] || [[ "x86_64" == "x86_64" ]] ; then
  ../ro/babymarvel 2>/dev/null
else
  qemu-x86_64 ../ro/babymarvel 2>/dev/null
fi