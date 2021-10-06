# this is a script file for chapter 6 exercise 3
# write a function named 'count' that accepts any string and a letter
# returns the number of times that letter occurs in the string

def count(a, b):
    x = 0
    for inc in a: 
        if inc == b:
            x += 1
    return x
    

if __name__ == '__main__':
    word = input("please enter a string: ")
    letter = input("please enter a letter to check: ")
    
    output = count(word, letter)
    print(output)
    


    