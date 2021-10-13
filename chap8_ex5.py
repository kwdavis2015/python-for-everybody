# script file for chapter 8 exercise 5
# read an mbox file, print out email senders and count total no. of emails

fname = input('Enter a file name: ')
fhand = open(fname)
emailcount = 0

for line in fhand:
    x = line.split()
    if len(x) == 0:
        continue 
    if x[0] != 'From':
        continue
    emailcount += 1
    print(x[1])
        
print('total number of emails in inbox: ', emailcount)