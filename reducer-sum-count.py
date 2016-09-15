#!/usr/bin/env python

import sys

salesTotal = 0
salesCount = 0

for line in sys.stdin:
    data = line.strip().split("\t")

    if len(data) != 2:
        continue

    thisKey, thisSale = data 
    salesTotal += float(thisSale)
    salesCount += 1

print "{0}\t{1}".format(salesTotal, salesCount)
