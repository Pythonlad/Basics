# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 17:04:04 2019

@author: Patrick
"""
"""
Assume s is a string of lower case characters.

Write a program that prints the number of times
 the string 'bob' occurs in s. For example,
 if s = 'azcbobobegghakl', then your program should print:
     Number of times bob occurs is: 2
"""
s = "bob where bob everbob sleep last nibobob, bob I don't boby"

bob = 0
for i in range(len(s)):
    if s[i] == 'b' and s[i+1] == 'o' and s[i+2] == 'b':
        bob+=1
print("Number of bobs is ", bob)
            
               
