# -*- coding: UTF-8 -*-


'''
Last modified time: 2014-12-17 11:24:40
Edit time: 2014-12-17 11:25:06
File name: def_map.py
Edit by caimaoy
'''


def _trans(c):
    ret = c
    ord_c = ord(c)
    max_ord = ord('z')
    if ord_c >= ord('a') and ord_c <= ord('z'):
        ord_c = ord_c + 2
        if ord_c > max_ord:
            ord_c -= 26
        ret = chr(ord_c)
    return ret

def _main(s):
    ret = []
    for i in s:
        ret.append(_trans(i))
    return ''.join(ret)


from string import lowercase, maketrans

text = 'g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr\'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'

def trans(s):
    alph_map = maketrans(lowercase, lowercase[2:]+lowercase[:2])
    return s.translate(alph_map)

if __name__ == '__main__':
    # print _main('dkfjdlfkdkfjdkfdjkdk9)kjsdlkfjskj fsdf3')
    '''
    print _trans('d')
    print _trans('z')
    '''
    # print _main(s)
    # print _main('map')
    print trans(text)


