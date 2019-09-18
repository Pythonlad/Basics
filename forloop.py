# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 11:30:49 2019

@author: Patrick
"""
"""
range(start, stop, step)
"""
#for i in range(10):
#    print(i)#prints all values from 0 to 9
#
#for i in range(5,10):
#    print(i)#prints 5 to 9

#print the sum of values btn 50 and 1000, step = 50.
theSum = 0
for i in range(50,1001,50): 
    theSum+=i
print(theSum)
