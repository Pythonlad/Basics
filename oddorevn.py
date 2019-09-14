# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 16:31:50 2019

@author: Patrick
"""

print("Give me a number, I tell u if it's even or odd")
number = int(input("Enter number: "))
if number % 2 == 0:
    print(number, "is even")
else:
    print(number, "is odd")
