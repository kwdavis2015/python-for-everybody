# script file for chapter 9 exercise 2
# read an mbox file and save a dictionary with the days of week mail was received

fname = input('enter a file name: ')

#try/except loop to validate a proper filename was entered
try:
    fhand = open(fname)
    
except: 
    print('filename cannot be opened: ', fname)
    exit()
    
dow = dict() # day of week in mbox file
    
for line in fhand:
    words = line.split()
    if len(words) == 0: 
        continue
    if words[0] != 'From': 
        continue
    x = words[2] # capture day of the week as a string on a valid line
    dow[x] = dow.get(x,0) + 1
    
print(dow)
