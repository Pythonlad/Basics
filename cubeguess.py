# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 13:36:03 2019

@author: Patrick
"""

#calculating the cube of a whole number
cuberoot = int(input("Enter a number: "))
guess = 0
while guess < abs(cuberoot**3):
    guess+=1
if cuberoot < 0:
    guess = -guess
print(guess)
