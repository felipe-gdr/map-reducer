#!/usr/bin/env python

import sys

count = 0
oldKey = None

for line in sys.stdin:
    data = line

    thisKey = data.rstrip() 

    if oldKey and oldKey != thisKey:
        print "{0}\t{1}".format(oldKey, count)
        count = 0

    oldKey = thisKey
    count += 1

print oldKey
if oldKey != None:
    print "--{0}\t{1}".format(oldKey, count)
