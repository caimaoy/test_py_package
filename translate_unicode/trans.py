# -*- coding: UTF-8 -*-

'''
Last modified time: 2014-12-03 09:35:04
Edit time: 2014-12-03 09:35:24
File name: trans.py
Edit by caimaoy
'''



import sets

class Keeper(object):
    def __init__(self, keep):
        self.keep = sets.Set(map(ord, keep))

    def __getitem__(self, n):
        if n not in self.keep:
            return None
        return unichr(n)

    def __call__(self, s):
        return unicode(s).translate(self)

makefilter = Keeper


def _test():
    just_vowels = makefilter('aeiou')
    print just_vowels('jkdjkf3eoirjnkdlsfjaslkdflkaf')
    print just_vowels(u'jkdjkf3eoirjnkdlsfjaslkdflkaf')

    chinese_test = makefilter(u'时间到金的副理圣节可的克风时间流世家')
    print = chinese_test(u'时间到了非金属的了副经理圣诞节是可敬的福克斯将风流世家')


def _main():
    _test()

if __name__ == '__main__':
    _main()
