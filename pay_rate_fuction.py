# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 21:20:38 2021

@author: kwdch
"""

def computepay(xhours, yrate):
    if xhours > 40: 
        extra = xhours - 40
        pay = (40*rate) + (extra*yrate*1.5)
    else: 
        pay = xhours * yrate 
    return pay

try: 
    hours = float(input("enter hours worked: "))
    rate = float(input("enter pay rate: "))
    
    x = computepay(hours, rate)
    
    print("pay equals " + str(x))

except: 
    print("Please enter a valid number for hours/rate")