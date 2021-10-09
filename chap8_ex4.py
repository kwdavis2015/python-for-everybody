# this is a script file for chapter 8 exercise 4
# read in a file and print out all unique words in the text file

fhand = open('practicefiles/romeo.txt')
u = [] #list var to capture all unique words 

for line in fhand:
    words = line.lower().split() #make everything lower case and split into list
    for x in words:
        if x in u:
            continue 
        u.append(x)
        
u.sort()
print('The list of unique words:\n', u)