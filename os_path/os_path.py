# -*- coding: UTF-8 -*-

import os

print __file__
GLOBAL_FILE = os.path.abspath(__file__)
print GLOBAL_FILE
dirname =  os.path.dirname(GLOBAL_FILE)
print os.path.dirname(dirname)
