# this is a script file for chapter 8 exercise 1
# description: write a function Chop that modifies a list and returns none
# write a second function called Middle that takes a list and returns a list 
# with first and last elements removed 

def chop(a):
    del a[0]
    del a[len(a)-1]
    return None 

def middle(b):
    chop(b)
    return b