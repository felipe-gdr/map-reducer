#!/usr/bin/env python

import sys

higherKey = None
higherCount = 0
oldKey = None
currentCount = 0

#print "comeco", currentCount, higherCount, higherKey, oldKey

for line in sys.stdin:
    data = line

    thisKey = data.rstrip() 

    if oldKey and oldKey != thisKey:
        #print higherKey, currentCount, higherCount
        if (higherKey == None or currentCount > higherCount):
            #print "new higher count: {0}, {1}".format(oldKey, currentCount)
            higherKey = oldKey
            higherCount = currentCount
        
        currentCount = 0

    oldKey = thisKey
    currentCount += 1


print "{0}\t{1}".format(higherKey, higherCount)
