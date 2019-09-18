# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 12:27:06 2019

@author: Patrick
"""
number = 0
#while True:
#    if number < 7:
#        print("breaking out of loop")
#        break
#    number-=1
#    print(number)
#print("outside of loop")

while number < 7:
    number +=1
    print("outside loop", number)
    while True:
        if number > 7:
            print("Breaking out of inner loop")
            break
        number +=1
        print(number)
    print("Out of inner loop")
print("Out of all loops")
