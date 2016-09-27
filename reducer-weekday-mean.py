#!/usr/bin/env python

import sys

salesDay = 0
countDay = 0
oldDay = None

for line in sys.stdin:
    data = line.strip().split("\t")

    if len(data) != 2:
        continue

    thisDay, thisSale = data

    if oldDay and oldDay != thisDay:
        print "{0}\t{1}".format(oldDay, (salesDay/countDay))

        salesDay = 0.
        countDay = 0 

    oldDay = thisDay
    salesDay += float(thisSale)
    countDay += 1

if oldDay != None:
    print "{0}\t{1}".format(oldDay, (salesDay/countDay))
