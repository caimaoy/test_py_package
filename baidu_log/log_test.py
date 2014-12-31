# -*- coding: UTF-8 -*-

'''
Last modified time: 2014-09-12 11:49:58
Edit time: 2014-09-12 11:54:10
File name: log_test.py
Edit by caimaoy
'''

import log
# import py_file


def main():
    logger = log.init_log('./log/my_test_log.txt')
    # log.logging.debug('debug test')
    logger.info('info test')

if __name__ == '__main__':
    main()
