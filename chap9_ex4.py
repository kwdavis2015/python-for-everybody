# script file for chapter 9 exercise 4
# read an mbox file and save a dictionary with all email addresses
# print out email address with maximum count  

fname = input('enter a file name: ')

#try/except loop to validate a proper filename was entered
try:
    fhand = open(fname)
    
except: 
    print('filename cannot be opened: ', fname)
    exit()
    
doe = dict() # dictionary of emails 
    
for line in fhand:
    words = line.split()
    if len(words) == 0: 
        continue
    if words[0] != 'From': 
        continue
    x = words[1] # capture day of the week as a string on a valid line
    doe[x] = doe.get(x,0) + 1

emailmax = ''
xmax = 0

for key in doe: 
    if doe[key] > xmax:
        xmax = doe[key]
        emailmax = key

print(emailmax, xmax)

