#coding:utf-8
import os, sys
from scs import SCSBox
import logging
import time

def initlog():

    """��ȡ��־���"""
    formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")

    hdlr  = logging.FileHandler("Failed.log", "ab")
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
    
    def __init__(self, sfile, sdown):
        self.filepath = sfile
        self.downpath = sdown
        self.login()
        
    def login(self):
        self.scsbox = SCSBox("store.bav.baidu.com", 80, "bcollecter", "bavbc1234qwer")
        
    def filestat(self, md5):
        #dict = self.scsbox.stat_file(md5)
        #print dict["file_size"]
        #return dict["existed"]
        return True
        
    def getfile(self, md5):
        savepath = os.path.join(self.downpath, md5)
        if self.filestat(md5):
            if self.scsbox.get_to_file(md5, savepath):
                logger.debug("%s-->���سɹ�." % md5)
            else:
                logger.info("%s-->����ʧ��." % md5)
        else:
            logger.info("%s-->�ļ�������." % md5)

    def DownSample(self):
        f = open(self.filepath, "r")
        data = f.read()
        f.close()
    
        md5lst = data.split("\n")
        nCnt = len(md5lst)
        print "һ��%d���ļ�." % nCnt
        index = 0
        for md5 in md5lst:
            md5 = md5.strip()
            if 32 != len(md5):
                continue
            nTry = 0
            index += 1
            print "%d/%d. MD5:%s" % (index, nCnt, md5)
            while True:
                try:
                    self.getfile(md5)
                    break
                except Exception, e:
                    #print e        #������Ϣ
                    nTry += 1
                    print "%s:���س���,���Ե�%d��." % (md5, nTry)
                    #os.system('pause')
                    #self.login()
                    if 3 == nTry:
                        logger.info("%s-->���ط�������." % md5)
                        break
            print ""


        
if __name__ == "__main__":
    t1 = time.time();
    if 3 != len(sys.argv):
        print "��������ȷ,����һ����ҪMD5�б��ļ� �� ��������Ŀ¼\n------------------------------------------------"
        print "Ĭ��MD5�ļ�: MD5.txt"
        print "Ĭ������Ŀ¼: Down\n------------------------------------------------"
        #Query = raw_input("�Ƿ�ʹ��Ĭ������?(Y/N)")
        #if Query.upper() == "Y":
        md5lst = os.path.join(os.getcwd(), "MD5.txt")
        downpath = os.path.join(os.getcwd(), "Down")
    else:
        md5lst = sys.argv[1]
        downpath = sys.argv[2]
        
    if not os.path.exists(md5lst):
        print "MD5.txt�ļ�������"
        os.system("pause")
        exit(0)
        
    if not os.path.exists(downpath):
        os.makedirs(downpath)
        
    print "ws"
    for fname in os.listdir(downpath):
        sfile = os.path.join(downpath, fname)
        if os.path.isfile(sfile):
            os.remove(sfile)    #���Ŀ¼
    GS = clsGetSample(md5lst, downpath)
    GS.DownSample()
    t2 = time.time();
    print "use time: %f" % (t2-t1)
    os.system("pause");
