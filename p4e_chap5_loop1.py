# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 12:03:05 2021

@author: kwdch
"""





x = 0
total = 0
i = 0
avg = 0

while True:
    inputNum = input("Enter a number: ")
    
    if inputNum == 'done':
        break 
    
    try: 
        if inputNum != 'done':
            x = int(inputNum)
            i += 1
            total = float(total + x)
            avg = float(total / i)
            
    except: 
        print("invalid input try again")

print(total, i, avg)
