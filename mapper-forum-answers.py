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
    body      = line[4]
    node_type = line[5]
    parent_id = line[6]

    order = 1
    if node_type == 'answer':
        order = 2
        id = parent_id


 
    print "{0}\t{1}\t{2}\t{3}\t{4}".format(int(id), order, node_type, parent_id, len(body))
