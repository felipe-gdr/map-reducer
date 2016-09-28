#!/usr/bin/env python

import sys
import operator

countHours = {}
oldAuthor = None

for line in sys.stdin:
    data = line.split("\t")

    if len(data) < 2:
        continue

    thisAuthor, hour = data

    if oldAuthor and oldAuthor != thisAuthor:
        topCount = max(countHours.iteritems(), key=operator.itemgetter(1))[1]

        topHours = {k: v for k, v in countHours.iteritems() if v == topCount}
     
        for h, c in topHours.iteritems(): 
            print "{0}\t{1}".format(oldAuthor, h)
 
        countHours = {}
    
    oldAuthor = thisAuthor

    hour = hour.replace('\n', '')
    if hour not in countHours:
        countHours[hour] = 1
    else:
        countHours[hour] += 1

if oldAuthor: 
    topCount = max(countHours.iteritems(), key=operator.itemgetter(1))[1]
    topHours = {k: v for k, v in countHours.iteritems() if v == topCount}
     
    for h, c in topHours.iteritems(): 
        print "{0}\t{1}".format(oldAuthor, h)
