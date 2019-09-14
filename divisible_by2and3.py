# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 18:02:53 2019

@author: Patrick
"""

#check if a number is divisible by 2 or 3 or both
print("Enter a number to check.")
number = int(input("Enter a number: "))

if(number % 2 == 0):
    if number % 3 == 0 :
        print(number, "is divisible by 2 and 3")
    else:
        print(number, "is divisible by 2 and not 3")
elif number % 3 == 0:
    print(number, "is divisible by 3 and not 2")
else:
    print(number, "is not divisible by 2 and 3")
    
