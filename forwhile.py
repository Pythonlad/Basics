# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 16:51:18 2019

@author: Patrick
"""
#different loops, same output...nice one.

#iterations = 0
#count = 0
#while iterations < 5:
#    for i in "hello, world":
#        count+=1
#    print("iteration",iterations,"count is",count)
#    iterations+=1


count = 0
phrase = "hello, world"
#for i in range(5):
#    x = 0
#    while x < len(phrase):
#        x+=1
#        count+=1
#    print("iteration",i,"count is",count)

for i in range(5):
    while True:
        count += len(phrase)
        break
    print("iteration",i,"count is",count)
    

#for i in range(5):
#        count += len(phrase)
#        print("iteration",i,"count is",count)





