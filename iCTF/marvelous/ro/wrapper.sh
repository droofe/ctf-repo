#!/bin/bash

cd /opt/ctf/marvelous/rw

if [[ "i386" == "x86_64" ]] || [[ "x86_64" == "x86_64" ]] ; then
  ../ro/marvelous 2>/dev/null
else
  qemu-x86_64 ../ro/marvelous 2>/dev/null
fi