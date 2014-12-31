# -*- coding: UTF-8 -*-

'''
Last modified time: 2014-09-15 11:37:08
Edit time: 2014-09-15 11:37:30
File name: dll_test.py
Edit by caimaoy
'''

import os
import ctypes
import global_path
import sqlite3
import time

import log_caimaoy
import bk_keyword as keyword


log = log_caimaoy.init_log('./log/test_bavwl')

def singleton(cls, *args, **kw):
    r'''单例模式装饰器
    '''

    instances = {}
    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return _singleton


@singleton
class BavWl_db(object):
    r'''数据库单例

    单例模式每次返回同一个实例db
    '''
    def __init__(self,
        db_path=global_path.bav_bavwl_path):
        r'''
        默认BavWl.dat数据库
        '''
        self.db_path = db_path
        self.db = connect_db(self.db_path)

    def get_db(self):
        return self.db


def connect_db(path):
    '''
    连接数据库
    '''
    db = None
    try:
        db = sqlite3.connect(path)
    except Exception, e:
        log.error(e)
        exit(1)

    if db:
        log.debug('connect db %s success %s'% (path, db))
    return db

'''
cx = sqlite3.connect('test.db')

#cx.execute('create table test(id integer primary key, pid integer, name varchar(10) UNIQUE, nickname text NULL)')
cx.execute('create table if not exists test(id integer primary key autoincrement, pid integer, name varchar(10), nickname text NULL)')
for t in [(1,'abc', 'df'), (23,'dfh', 'dfd')]:
    cx.execute('insert into test values (NULL,?,?,?)', t)
cx.commit()

cur = cx.cursor()
# cur.execute('select * from test')
cur.execute('select * from test where id = (select max(id) from test)')
# 第二大id
cur.execute('select * from (select * from test order by id desc limit 2) order by id limit 1')
print cur.fetchall()

'''

def is_file_table(file_name, table_name):
    cur = BavWl_db().get_db().cursor()
    for row in cur.execute('select * from wl_unknown_file_type_file where FileName = ?',(file_name, )):
        print row


class Query_file_in_table(object):
    def __init__(self, select_item='*',
                  table='wl_unknown_file_type_file',
                  where='FileName'):
        self.select_item = select_item
        self.table = table
        self.where = where
        self.init()
        log.debug('base sql is \'%s\''%self.sql)

    def init(self):
        self.sql = 'select %s from %s'% (self.select_item,
                                         self.table)
        if self.where:
            self.sql = ''.join([self.sql, ' where %s = ?'%self.where])

    def is_in_table(self, where_item):
        cur = BavWl_db().get_db().cursor()
        '''
        for row in cur.execute(self.sql, (where_item, )):
            print row
        '''
        ret = False
        for row in cur.execute(self.sql, (where_item, )):
            if row:
                ret = True
                log.debug('%s is in %s'% (where_item, self.table))

        if ret is False:
            log.debug('%s is not in %s'% (where_item, self.table))
        return ret


def crc32(s, dll_path=global_path.bav_common_dll_path):
    '''载入BavCommon.dll使用其crc32函数

    crc32 函数原型
    unsigned long crc32(
        unsigned long crc,
        const unsigned char *buf,
        unsigned len
        );

    输入s 必须为unicode编码，len为wstrTemp.length() * sizeof(wchar_t)
    也就是说python 传入的第三个参数为len(str) * 2
    TODO 这个地方好像不用每次都加载，可以优化
    '''
    ret = 0
    try:
        dll = ctypes.WinDLL(dll_path)
        foo = dll.crc32
        foo.restype = ctypes.c_ulong
        ret = foo(ctypes.c_ulong(0), unicode(s), (len(s) + 0) * 2)
    except Exception, e:
        log.error(e)
        exit(1)
    return ret


def str2key(s):
    '''
    文件名2KEY 二次加速复杂的计算方式,骚年看文档去吧
    '''
    s = s.lower()
    file_name_crc32 = crc32(os.path.basename(s))
    dir_name_crc32 = 0
    dir_name = os.path.dirname(s)
    # print 'dir_name is %s'% dir_name
    if(dir_name.endswith('\\')):
        # \\结尾表示已经是更目录了,只有一层目录
        dir_name_crc32 = crc32(dir_name)
    else:
        # 有两层以上目录
        base_name_se = os.path.basename(dir_name)
        dir_name_se = os.path.dirname(dir_name)

        if(dir_name_se.endswith('\\')):
            # 去掉\
            dir_name_se = dir_name_se[:-1]

        low_32_crc = crc32(base_name_se)
        high_32_crc = crc32(dir_name_se)

        dir_name_crc32 = (high_32_crc & 0xffff0000 |
                          low_32_crc & 0x0000ffff)

    ret = dir_name_crc32 << 32 | file_name_crc32
    ret = ctypes.c_longlong(ret)
    return ret.value


class Test_insert_bavwl(object):
    '''二次加速入库检查
    '''

    table2file = {'wl_donot_scan_file': './bavwl_file/donnot_scan.asp',
                  'wl_gray_none_pe_cloud_scan_file': './bavwl_file/NonePe.EXE',
                  'wl_document_scan_file': './bavwl_file/document.html',
                  'wl_script_scan_file': './bavwl_file/script.php',
                  'wl_unknown_file_type_file': './bavwl_file/unkown.dmp',
                  'wl_compressed_file': './bavwl_file/compress.rar',
                  'wl_fi_file_type_file': './bavwl_file/fi_file.exe',
                  'wl_gray_pe_cloud_scan_file_with_md5_micro_signs': './bavwl_file/double_gray.dll',
                  'wl_sign_to_white_file': './bavwl_file/python.exe',
                  'wl_micro_sign_white_file': './bavwl_file/micro_white.exe',
                  'wl_gray_pe_cloud_scan_file': './bavwl_file/single_gray',
                  }

    dir_path = './bavwl_file'

    def __init__(self):
        pass

    def test_insert(self, table_name):
        i_test = Query_file_in_table(table=table_name,
			                         where='FileName')
        file_path = os.path.abspath(self.table2file[table_name])

        #扫描之前查找是否入库
        is_file_in_db = i_test.is_in_table(str2key(file_path))
        if is_file_in_db is True:
            # del bavwl
            log.debug('del bavwl.dat')
        else:
            #scan
            log.debug('scan file: %s' % file_path)
            keyword.right_click2(file_path)
            # 大坑 我如何知道扫描结束了?
            time.sleep(5)

        ret = i_test.is_in_table(str2key(file_path))
        if ret is True:
            log.debug('%s in %s pass'%(file_path, table_name))
        else:
            log.error('%s in %s failed'%(file_path, table_name))
        return ret


    def test_insert_all(self, table_name_list):
        def is_in_table(table, file):
            '''
            复制的查询过程封装
            '''
            q = Query_file_in_table(table=table, where='FileName')
            print os.path.abspath(file)
            k = str2key(os.path.abspath(file))
            return q.is_in_table(k)
        
        
        is_in_db = False

        for i in table_name_list:
            if is_in_table(i, self.table2file[i]):
                is_in_db = True
                break
        if is_in_db:
            # del bavwl
            pass

        scan_path = os.path.abspath(self.dir_path)
        keyword.right_click2(scan_path)
        time.sleep(20)

        failed_case = []
        for i in table_name_list:
            if is_in_table(i, self.table2file[i]):
                pass
                log.debug('\'%s\' is in %s.'% (self.table2file[i], i))
            else:
                s = '\'%s\' insert %s failed!'% (self.table2file[i], i)
                failed_case.append(s)
        ret = False
        if failed_case:
            log.error('Failed cases are %s!'% failed_case)
            print 'Failed cases are %s!'% failed_case
            ret = False
        else:
            log.info('All cases pass')
            ret = True
        return ret


    def __all_test_one_by_one(self):
        '''
        每个表每种文件扫描一次，会有扫描结束的坑，同时多次扫描花费很多时间
        '''
        ret = False
        test = Test_insert_bavwl()
        false_case_list = []
        case_result_set = set()
        for i in self.table2file:
            r = test.test_insert(i)
            if r is False:
                s = 'insert %s failed'% i
                false_case_list.append(s)
                case_result_set.add(False)
            else:
                case_result_set.add(True)
        if False in case_result_set:
            log.error('Failed case are %s'% false_case_list)
            print 'Failed case are %s'% false_case_list
            ret = False
        if False not in case_result_set and True in case_result_set:
            log.info('All cases pass')
            ret = True
        return ret

    def __call__(self):
        return self.test_insert_all(self.table2file.keys())


def test_bavwl_foo():
    os.chdir(os.path.split(os.path.realpath(__file__))[0])
    return Test_insert_bavwl()()

if __name__ == '__main__':
    '''
    print str_2_key(u'D:\\caimaoy\\test\\新建文件夹 (2)\\新建文件夹\\新建文件夹\\python - 副本.exe')
    test = Test_insert_bavwl()
    test.test_insert('wl_donot_scan_file')
    '''
    test_bavwl_foo()
