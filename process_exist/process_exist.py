# -*- coding: UTF-8 -*-

'''
Last modified time: 2014-10-14 19:36:09
Edit time: 2014-10-14 19:36:33
File name: process_exist.py
Edit by caimaoy
'''

import win32com.client

def CheckProcExistByPN(process_name):
  try:
    WMI = win32com.client.GetObject('winmgmts:')
    processCodeCov = WMI.ExecQuery('select * from Win32_Process where Name="%s"' % process_name)
  except Exception,e:
    print process_name + "error : ", e;
    
  if len(processCodeCov) > 0:
    print process_name + " exist";
    return 1
  else:
    print process_name + " is not exist";
    return 0

def is_process_exist(p):
    ret = 0
    try:
        WMI = win32com.client.GetObject('winmgmts:')
        processCodeCov = WMI.ExecQuery('select * from Win32_Process where Name="%s"' % p)
    except Exception as e:
        print p + "error : ", e;
    if len(processCodeCov) > 0:
        ret = True
    else:
        ret = False
    return ret



if __name__ == '__main__':
    print is_process_exist('chrome.exe')
    print is_process_exist('BavSvc.exe')
    CheckProcExistByPN('chrome.exe')
