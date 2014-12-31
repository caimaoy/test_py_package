# -*- coding: UTF-8 -*-

import re

text = "JGood is a handsome boy, he is cool, clever, and so on..."
m = re.search(r"(\w+)\s", text)
if m:
    print m.group(0), '\n', m.group(1)
else:
    print 'not match'


print re.sub(r'\s+', '-', text) 
