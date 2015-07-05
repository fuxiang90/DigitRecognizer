#!/bin/env python
#!coding=utf8

import sys
from sklearn import linear_model
from common import loadTrain

class  Linear(object) :
    

    def __init__(self) :
        
        self.linear_model = linear_model.Ridge (alpha = .5)
        pass


    def work(self, trainfile, testfile) :
        
        # get train input 
        x ,y =  loadTrain(trainfile) 
        #train 
        self.linear_model.fit(x,y  ) 
        
        py = self.linear_model.predict(x) 

        notEqual = 0 
        for each in range(len(py) ) :
            if py[each] != y[each] :
                notEqual += 1

        print notEqual
    
        pass


if __name__ == '__main__':


    obj = Linear() 

    obj.work(sys.argv[1], sys.argv[2] ) 


