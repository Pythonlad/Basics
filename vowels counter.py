# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 12:44:25 2019

@author: Patrick
"""

school = "Massachussets Institute of Technology"
numVowels = 0
numCons = 0
for letter in school:
    if letter == 'a' or letter == 'e' or letter == 'i'\
    or letter == 'o' or letter == 'u':
        numVowels += 1
    elif letter == ' ':#skip spaces
        pass
    else:
        numCons +=1
print("Number of consonants is " + str(numCons))
print("Number of vowels is " + str(numVowels))
print(len(school))       
