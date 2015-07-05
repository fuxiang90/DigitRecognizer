#!/bin/env python 

import sys

def loadTrain(filename):
    
    pos = 0 
    label = []
    vector = []
    for line in open(filename) :
        
        if pos != 0 :
            lineList = line.strip().split(',')
            label.append( int(lineList[0]) ) 
            vector.append( [ int(x) for x in lineList[1:] ] ) 

        pos += 1

    return vector, label

def loadTest(filename):
    
    pos = 0 
    vector = []
    for line in open(filename) :
        
        if pos != 0 :
            lineList = line.strip().split(',')
            vector.append( [ int(x) for x in lineList ] ) 

        pos += 1

    return vector

