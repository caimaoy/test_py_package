#coding:utf-8
import os, sys
from scs.scs import SCSBox
import logging

def initlog():

    """��ȡ��־���"""
    formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")

    hdlr  = logging.FileHandler("sample_status.log", "w")
    hdlr.setLevel(logging.INFO)
    hdlr.setFormatter(formatter)

    hds = logging.StreamHandler()
    hds.setLevel(logging.DEBUG)
    hds.setFormatter(formatter)

    logger = logging.getLogger("123")
    logger.setLevel(logging.DEBUG)
    logger.addHandler(hdlr)
    logger.addHandler(hds)
    return logger

logger = initlog()

class clsGetSample(object):
    
    def __init__(self, sfile):
        self.filepath = sfile
        self.login()
        
    def login(self):
        self.scsbox = SCSBox("bcollecter", "bavbc1234qwer")
        
    def filestat(self, md5):
        try:
            dict = self.scsbox.stat_file(md5)
        except:
            return {"existed":0, "source":'0'}
        print dict
        os.system('pause')
        return dict
        
    def DownSample(self):
        f = open(self.filepath, "r")
        data = f.read()
        f.close()
    
        md5lst = data.split("\n")
        nCnt = len(md5lst)
        print "MD5 COUNT:%d" % nCnt
        index = 0
        exists = {0:'no', 1:'have'}
        dt = {}
        for md5 in md5lst:
            #md5 = md5.strip()
            md5 = md5[0:32]
            #if 32 != len(md5):
            #    continue
            dt = self.filestat(md5)
            source = '0'
            if dt.has_key('source'):
                source = dt['source']
            nTry = 0
            index += 1
            print "%d/%d. MD5:%s" % (index, nCnt, md5)
            logger.info('%s:%d:%s' % (md5, dt['existed'], source))

        
if __name__ == "__main__":

    if 2 != len(sys.argv):
        #Query = raw_input("�Ƿ�ʹ��Ĭ������?(Y/N)")
        #if Query.upper() == "Y":
        md5lst = os.path.join(os.getcwd(), "MD5.txt")
    else:
        md5lst = sys.argv[1]
        
    if not os.path.exists(md5lst):
        print "not found MD5.txt"
        os.system("pause")
        exit(0)


    GS = clsGetSample(md5lst)
    GS.DownSample()
    os.system("pause")