# script file for chapter 9 exercise 5
# read an mbox file and save a dictionary with all email address domains
# count how many times each domain occurs and print dict object at end

fname = input('enter a file name: ')

#try/except loop to validate a proper filename was entered
try:
    fhand = open(fname)
    
except: 
    print('filename cannot be opened: ', fname)
    exit()
    
schoolcount = dict() # dictionary of email domains
    
for line in fhand:
    words = line.split()
    if len(words) == 0: 
        continue
    if words[0] != 'From': 
        continue
    x = words[1]
    a = x.find('@') # capture where domain begins   
    x = x[a+1:]
    schoolcount[x] = schoolcount.get(x,0) + 1

print(schoolcount)
