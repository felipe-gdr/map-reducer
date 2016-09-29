#!/usr/bin/env python
import sys
import re
import csv
from datetime import datetime

patternW = re.compile('[ \.,!?:;\"\(\)<>\[\]\#\$\=\-/]')

reader = csv.reader(sys.stdin, delimiter='\t', quoting=csv.QUOTE_ALL, quotechar = '"') 

for line in reader:
    if line[0] == 'id':
        continue

    for tag in line[2].split(" "):
        if len(tag) > 0:
            print "{0}".format(tag)
