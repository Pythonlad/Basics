# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 18:30:45 2019

@author: Patrick
"""

#Determining least of three numbers
print("Enter three numbers")
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))

if z < y and z < x:
    print(z," is the least")
elif y < x:
    print(y, " is the least")
else:
    print(x, " is the least")
    
