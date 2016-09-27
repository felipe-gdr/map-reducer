#!/usr/bin/env python
import sys
import re
import csv

patternW = re.compile('[ \.,!?:;\"\(\)<>\[\]\#\$\=\-/]')

reader = csv.reader(sys.stdin, delimiter='\t', quoting=csv.QUOTE_ALL, quotechar = '"') 

for line in reader:
    body =  line[4]
    nodeId = line[0]

    for w in patternW.split(body):
        w = w.lower()
        if len(w) > 0:
            print "{0}\t{1}".format(w,nodeId)
