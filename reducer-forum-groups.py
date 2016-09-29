#!/usr/bin/env python

import sys
import operator

oldQuestion  = None
participants = []

for line in sys.stdin:
    data = line.split("\t")

    if len(data) < 2:
        continue

    thisQuestion, author = data

    if oldQuestion and oldQuestion != thisQuestion:
        print "{0}\t{1}".format(oldQuestion, participants)
 
        participants = [] 
    
    oldQuestion = thisQuestion
    participants.append(author.replace('\n', ''))

if oldQuestion: 
    print "{0}\t{1}".format(oldQuestion, participants)
 
