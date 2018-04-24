#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-12 17:31:39
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os
import time

def main(n):
    path = "/home/shared/upload/"
    files = os.listdir(path)
    for file in files:
        t = os.path.getctime(path+file)
        if time.time() - t > 604800:
            os.remove(path+file)
    time.sleep(n)

main(86400)
