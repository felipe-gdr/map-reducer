#!/usr/bin/env python

import sys
import operator

oldTag  = None
countTag = 0
top10 = []

def changeTag(top10, countTag, oldTag): 
    if len(top10) == 10:
        lowerTop10 = min(row[1] for row in top10)

        if countTag > lowerTop10:
            top10[9] = [oldTag, countTag]
        
    else:
        top10.append([oldTag, countTag])       
       
    # Sort top 10 list
    return sorted(top10, key=lambda r:r[1], reverse=True)


for line in sys.stdin:
    thisTag = line.replace('\n', '') 

    if oldTag and oldTag != thisTag:
        top10 = changeTag(top10, countTag, oldTag)
        countTag = 0

 
    oldTag = thisTag
    countTag += 1

top10 = changeTag(top10, countTag, oldTag)

if top10:
    for top in top10:
        print "{0}\t{1}".format(top[0], top[1])


