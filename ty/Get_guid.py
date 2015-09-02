'''
Created on 2015-2-10

@author: tangyin02
'''
import os,sys
import string

def read(src,drc="C:\\guid.txt"):
    file = open(src,'r')
    file2 = open(drc,'w')
    line = file.readline()
    while line:
        line = line.lower()
        # print line
        file2.write(line)
        file2.flush()
        line = file.readline()
    file.close()
    file2.close()

if __name__ == '__main__':
    # print sys.argv[1]
    read(sys.argv[1])
    pass
