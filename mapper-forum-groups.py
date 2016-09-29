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

    id        = line[0]
    author    = line[3]
    node_type = line[5]
    parent_id = line[6]

    if node_type == 'answer':
        id = parent_id


 
    print "{0}\t{1}".format(int(id), author)
