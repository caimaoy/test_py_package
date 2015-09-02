# -*- coding: UTF-8 -*-

'''
Last modified time: 2015-04-16 14:03:38
Edit time: 2015-04-16 14:03:55
File name: test_argparse.py
Edit by caimaoy
'''

__author__ = 'caimaoy'


import argparse

parser = argparse.ArgumentParser(description="calculate X to the power of Y")
group = parser.add_mutually_exclusive_group()
group.add_argument("-v", "--verbose", action="store_true")
group.add_argument("-q", "--quiet", action="store_true")
parser.add_argument("x", type=int, help="the base")
parser.add_argument("y", type=int, help="the exponent")
args = parser.parse_args()
answer = args.x**args.y

if args.quiet:
    print answer
elif args.verbose:
    print "{} to the power {} equals {}".format(args.x, args.y, answer)
else:
    print "{}^{} == {}".format(args.x, args.y, answer)


if __name__ == '__main__':
    pass
