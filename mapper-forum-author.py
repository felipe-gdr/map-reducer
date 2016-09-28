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

    author    = line[3]
    dateAdded = line[8]
 
    hour = datetime.strptime(dateAdded.split(':')[0], "%Y-%m-%d %H").hour
    print "{0}\t{1}".format(author, hour)
