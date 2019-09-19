# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 13:14:50 2019

@author: Patrick
"""

#Find the cuberoot using guess and check.
#Takes care of even negative numbers
cube = int(input("Enter a number: "))

cuberoot = 0
while cuberoot**3 < abs(cube):
    cuberoot+=1
if cuberoot**3 != abs(cube):
    print(cube,"is not a perfect cube")
else:
    if cube < 0:
        cuberoot = -cuberoot
    print("The cuberoot of ", cube, "is",cuberoot)
        
        
