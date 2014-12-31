# -*- coding: UTF-8 -*-


print 'aaa'
import ConfigParser
conf = ConfigParser.ConfigParser()
filepath = r'config.txt'
conf.read(filepath)
src_file = conf.get('file', 'src_file')
print src_file


import os
import time
i = 100
while(1):
    des_file = os.path.join(os.getcwd(), src_file+'copy'+str(i))
    print des_file
    open(des_file, "wb").write(open(src_file, "rb").read())
    time.sleep(3)
    i = i - 1
    if i == 0:
        break
