#!/bin/bash

cd /opt/ctf/hero_text_adventure/rw

if [[ "i386" == "x86_64" ]] || [[ "x86_64" == "x86_64" ]] ; then
  ../ro/hero_text_adventure 2>/dev/null
else
  qemu-x86_64 ../ro/hero_text_adventure 2>/dev/null
fi