#!/bin/bash

cd /opt/ctf/brave_rust/rw

if [[ "i386" == "x86_64" ]] || [[ "x86_64" == "x86_64" ]] ; then
  ../ro/brave_rust 2>/dev/null
else
  qemu-x86_64 ../ro/brave_rust 2>/dev/null
fi