#!/bin/sh
lib_path=LD_LIBRARY_PATH=/home/quyan/PycharmProjects/PyHttpServer/libsafe3
export $lib_path:$LD_LIBRARY_PATH
echo $LD_LIBRARY_PATH
python3 pyhttpserver.py
