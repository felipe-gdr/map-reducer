#!/usr/bin/env python

import sys
import operator

oldQuestion  = None
questionLen  = 0.
countAnswers = 0.
totalAnswLen = 0.

for line in sys.stdin:
    data = line.split("\t")

    if len(data) < 2:
        continue

    thisQuestion, order, node_type, parent_id, length = data

    if oldQuestion and oldQuestion != thisQuestion:
        avg = 0. if countAnswers == 0 else (totalAnswLen / countAnswers)
        print "{0}\t{1}\t{2}".format(oldQuestion, questionLen, avg)
 
        questionLen, countAnswers, totalAnswLen = 0., 0., 0.
    
    oldQuestion = thisQuestion

   
    length = float(length)
    if node_type == 'question':
        questionLen = length
    elif node_type == 'answer':
        countAnswers += 1
        totalAnswLen += length

if oldQuestion:
    avg = 0. if countAnswers == 0 else (totalAnswLen / countAnswers)
    print "{0}\t{1}\t{2}".format(oldQuestion, questionLen, avg)
 
