# -*- coding: UTF-8 -*-

'''
Last modified time: 2015-04-16 10:49:15
Edit time: 2015-04-16 10:49:27
File name: test_csv.py
Edit by caimaoy
'''

__author__ = 'caimaoy'


import csv

'''
with open('test.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print row['hash']

'''

with open('test.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print row

if __name__ == '__main__':
    pass
