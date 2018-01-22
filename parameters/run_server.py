#!/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'GuoJunmao'

import threading
import os

class RunServer(threading.Thread):
    def __init__(self, port):
        threading.Thread.__init__(self)
        self.cmd = 'macaca server -p %s --verbose' % port

    def run(self):
        os.system(self.cmd)