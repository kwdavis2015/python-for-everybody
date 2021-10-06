# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 20:57:15 2021

@author: kwdch
"""

try: 
    hours = float(input("please enter hours worked: "))
    rate = float(input("enter pay rate: "))
    
    if hours > 40: 
        extra = hours - 40
        pay = (40*rate) + (extra*rate*1.5)
    else: 
        pay = hours * rate 
    
    x = round(pay,2)
    
    print("pay equals " + str(x))

except: 
    print("Please enter a valid number for hours/rate")