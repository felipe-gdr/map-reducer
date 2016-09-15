#!/usr/bin/env python

import sys

highestSale = 0
oldKey = None

for line in sys.stdin:
    data = line.strip().split("\t")

    if len(data) != 2:
        continue

    thisKey, thisSale = data

    if oldKey and oldKey != thisKey:
        print "{0}\t{1}".format(oldKey, highestSale)

        highestSale = 0

    oldKey = thisKey

    #print highestSale, oldKey, thisKey, thisSale

    if float(thisSale) > float(highestSale):
	#print "is highest", thisSale, highestSale
        highestSale = float(thisSale)

if oldKey != None:
    print "{0}\t{1}".format(oldKey, highestSale)
