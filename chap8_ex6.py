# script file for chapter 8 exercise 6 
# ask a user for numbers until they enter 'done'
# print out max, min, and avg of the list

x = [] #blank list for user's numbers to go into
y = 0 
i = 0 
while True:
    inputNum = input('Enter a number: ')
    
    if inputNum == 'done':
        break 
    
    try: 
        if inputNum != 'done':
            y = int(inputNum)
            x.append(y)
            i += 1
          #  print(x) 
            
    except: 
        print('invalid input try again')

print('max number:', max(x), '\nmin number:', min(x))