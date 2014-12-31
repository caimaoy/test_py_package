# -*- coding: utf-8 -*-
'''
#=============================================================================
#  Author:          dantezhu - http://www.vimer.cn
#  Email:           zny2008@gmail.com
#  FileName:        xf.py
#  Description:     获取当前位置的行号和函数名
#  Version:         1.0
#  LastChange:      2010-12-17 01:19:19
#  History:         
#=============================================================================
'''
import sys
def get_cur_info():
    """Return the frame object for the caller's stack frame."""
    try:
        raise Exception
    except:
        f = sys.exc_info()[2].tb_frame.f_back
        print f
        memberlist = [m for m in dir(f)]
        _dict = {}
        for m in memberlist:
            if m[0] != '_' and not callable(m):
                _dict[m] = getattr(f, m)

        print _dict
        '''
        for k, v in _dict:
            print k, v
            # print '_dict[%s] is %s' % (k, v)
        '''

    return (f.f_code.co_name, f.f_lineno)
 
def callfunc():
    print get_cur_info()
 
 
if __name__ == '__main__':
    callfunc()
