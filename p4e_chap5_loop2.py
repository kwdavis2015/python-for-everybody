# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 12:03:05 2021

@author: kwdch
"""



# not working in current state...

x = 0
total = 0
i = 0
xmin = 0
xmax = 0

while True:
    inputNum = input("Enter a number: ")
    
    if inputNum == 'done':
        break 
    
    try: 
        if inputNum != 'done':
            x = int(inputNum)
            i += 1
            total = float(total + x)
            
            if i == 1: 
                xmin = x
                xmax = x 
                
            elif x > xmax: 
                xmax = x
                
            elif x < xmin: 
                xmin = x
            
    except: 
        print("invalid input try again")

print(total, i, xmin, xmax)