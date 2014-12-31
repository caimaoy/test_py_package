# -*- coding: UTF-8 -*-

'''
Last modified time: 2014-09-15 17:50:21
Edit time: 2014-09-15 17:51:42
File name: test_bavwl.py
Edit by caimaoy
'''

import logger
import ctypes

log = logger.init_log(r'./log/stamp_dll')

def test():
    '''
    QFILESIGLIB_API BOOL GetAuthSignTimeW(__in_z WCHAR* szFile, __out WCHAR* szTimeStr,__in int nTimeLen);
    '''
    dll_path = r'QFileSigLib.dll'
    ret = 0
    try:
        dll = ctypes.WinDLL(dll_path)
        foo = dll.GetAuthSignTimeW
        # foo.restype = ctypes.c_ulong
        #ret = foo(ctypes.c_ulong(0), unicode(s), (len(s) + 0) * 2)
        out = ctypes.c_wchar_p('0' * 30)
        # out = ctypes.create_string_buffer(100)
        file_name = ctypes.c_wchar_p(r'C:\Program Files (x86)\Baidu Security\Baidu Antivirus\BavCns.dll')
        '''
        file_name = ctypes.c_wchar_p()
        file_name.value = r'C:\Program Files (x86)\Baidu Security\Baidu Antivirus\BavCns.dll'
        '''
        # out.value = '0'*300
        print out
        print out.value
        print file_name

        foo.argtypes = [ctypes.c_wchar_p, ctypes.c_wchar_p, ctypes.c_int]
        o = foo(file_name, out, ctypes.c_int(30))
        print o
        print out.value

    except Exception as e:
        log.error(e)
        exit(1)
    return ret


if __name__ == '__main__':
    test()
