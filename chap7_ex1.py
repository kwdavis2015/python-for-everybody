# this is a file for chapter 7 exercise 1
# read through a file and print all contents capitalized

fname = input('enter a file name: ')

#try/except loop to validate a proper filename was entered
try:
    fhand = open(fname)
    
except: 
    print('filename cannot be opened: ', fname)
    exit()

#iterate through each line, remove \n, capitalize and print
for line in fhand:
    x = line.rstrip()
    x = x.upper()
    print(x)
    