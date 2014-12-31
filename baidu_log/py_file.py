# -*- coding: UTF-8 -*-

'''
Last modified time: 2014-09-12 11:49:58
Edit time: 2014-09-12 11:54:10
File name: log_test.py
Edit by caimaoy
'''

import log
import time


log.init_log('./log/my_test_log.txt')
log.logging.debug('debug test')
log.logging.info('info test')
log.logging.warning('warning test')

for i in range(5):
    time.sleep(3)
    log.logging.warning('warning test')
    log.logging.warning('%s'%i)

def main():
    log.init_log('./log/my_test_log.txt')
    # logging.debug('debug test')
    logging.info('info test')

if __name__ == '__main__':
    main()

