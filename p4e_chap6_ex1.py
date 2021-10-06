# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 16:33:01 2021

@author: kwdch
"""

s = input("Please input a string: ")
index = len(s)
i = 0

while i < len(s): 
    print(s[index-1])
    i += 1
    index -= 1