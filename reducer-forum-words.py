#!/usr/bin/env python

import sys

count = 0
oldWord = None
nodes = []

for line in sys.stdin:
    data = line.split("\t")

    if len(data) < 2:
        continue

    thisWord, node = data

    if oldWord and oldWord != thisWord:
        print "{0}\t{1}\t{2}".format(oldWord, count, nodes)
 
        nodes = []
        count = 0

    oldWord = thisWord
    count += 1
    nodes.append(node)

if oldWord != None:
    print "{0}\t{1}\t{2}".format(oldWord, count, nodes)
