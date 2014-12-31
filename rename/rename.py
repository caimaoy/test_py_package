# -*- coding: UTF-8 -*-

import os

if __name__ == '__main__':
    file_list = os.listdir(os.getcwd())
    for f in file_list:
        os.rename(f,f+'.exe')
