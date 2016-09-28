#!/usr/bin/python
# Here you will be able to combine the values that come from 2 sources
# Value that starts with A will be the user data
# Values that start with B will be forum node data

import sys

oldUser = None
userData = None
pendingNodes = []
for line in sys.stdin:
    data = line.split("\t")
    
    categ = data[1]
    thisUser = data[0]

    if oldUser and oldUser != thisUser:
        userData = None
  
    oldUser = thisUser

    if categ == 'A':
        if userData == None:
            pendingNodes.append(data) 
        else:
            print data + userData 
    elif categ == 'B':
        userData = data[2:]

        for pend in pendingNodes:
            print pend + userData

        pendingNodes = [] 
