# file for chapter 6 exercise five
# slice given string and convert end to floating point num


str = 'X-DSPAM-Confidence:0.8475'

x = str.find(':')
y = str[x+1:(len(str))]
z = float(y)

print(z)