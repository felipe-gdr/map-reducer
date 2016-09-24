#!/usr/bin/env python
import sys
import re

regex = '([(\d\.)]+) - - \[(.*?)\] "(.*?)" (\d+) - "(.*?)" "(.*?)"'

for line in sys.stdin:
    data = re.match(regex, line).groups


    ip, time, req, status, size = data 
    print "{0}\t{1}".format(ip, req)
