# this is a file for chapter 7 exercise 2
# read through a text file, find the matching line, and convert part of string to a number

fname = input('enter a file name: ')

#try/except loop to validate a proper filename was entered
try:
    fhand = open(fname)
    
except: 
    print('filename cannot be opened: ', fname)
    exit()

#iterate through each looking for target string, convert to num if match found
#total up the num values and compute total average of all confidence intervals

target = 'X-DSPAM-Confidence:'
lentarget = len(target)
count = 0
total = 0

for line in fhand:
    if len(line) > 0 and line[:lentarget] == target:
        x = float(line[lentarget:len(line)].strip())
        count += 1
        total = total + x

avg = total / count

print('the average spam confidence is:', avg)
