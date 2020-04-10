#!/usr/bin/env python3
# 
# Cross Platform and Multi Architecture Advanced Binary Emulation Framework
# Built on top of Unicorn emulator (www.unicorn-engine.org) 

import sys
sys.path.append("..")
from qiling import *

def my_sandbox(path, rootfs):
    ql = Qiling(path, rootfs, output = "debug")
    ql.multithread = True
    ql.run()


if __name__ == "__main__":
    my_sandbox(["rootfs/x8664_linux/bin/x8664_multithreading"], "rootfs/x8664_linux")
