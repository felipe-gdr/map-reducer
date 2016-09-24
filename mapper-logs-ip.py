#!/usr/bin/env python
import sys
import re

regex = '([(\d\.)]+) - - \[(.*?)\] "(.*?)" (\d+) (.+)'
pattern = re.compile(regex)

for line in sys.stdin:
    matcher = re.match(regex, line)

    if matcher:
        data = matcher.groups()
        ip, time, req, status, size = data 
        print "{0}".format(ip)
