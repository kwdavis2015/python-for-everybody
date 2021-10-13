# script file for chapter 9 exercise 1
# read a text file, save the words as strings in a dict object

fname = 'practicefiles/words.txt'
fhand = open(fname)

wordlist = dict()
i = 0 # use as key value for each word 
for line in fhand:
    x = line.split()
    for y in x: 
        wordlist.update({i: y})
        i += 1
        
print(wordlist)

