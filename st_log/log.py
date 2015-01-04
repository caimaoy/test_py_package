# -*- coding: UTF-8 -*-

'''
Last modified time: 2014-07-15 12:14:06
Edit time: 2014-07-15 12:15:39
File name: log.py
Edit by caimaoy
'''

'''
import logging
import logging.config
import sys
sys.path.append('..')

import common.global_path as Global



#print Global.CONF_PATH

# log_config_path = ''.join([Global.CONF_PATH, r'\log.conf'])
log_config_path = Global.join_work_path(r'conf\log.conf')
print log_config_path
# print log_config_path 
# E:\test-pc-av\baidu_security\pc_av\Src\daily_build\conf\log.conf
logging.config.fileConfig(log_config_path)
log = logging.getLogger('simple')
log.info('create log success! from log.py:)')
'''

import st_log


log = st_log.init_log(r'./test')
log.debug('test')
