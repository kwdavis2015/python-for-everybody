# this is a script file for chapter 8 exercise 2 and 3
# modify the given function and practice file to ensure proper guarding to avoid exceptions

fhand = open('practicefiles\mbox-short.txt')

for line in fhand:
    words = line.split()
    # print('Debug:', words)
    if len(words) == 0 : continue
    if words[0] != 'From' : continue
    print(words[2])