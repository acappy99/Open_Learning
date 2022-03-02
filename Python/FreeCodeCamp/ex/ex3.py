# Exercise (strings)
# 1. Use find and string slicing to extract the portion of the string after the colon
# character and then use the float function to convert the extracted string into a
# floating point number.

# 2. Read the documentation of the string methods at
# https://docs.python.org/library/stdtypes.html#string-methods
# You might want to experiment with some of them to make sure you understand how they work.
# strip and replace are particularly useful.


# .find()
print('')
str = 'X-DSPAM-Confidence: 0.8475'
print(str)
spos = str.find(' ')
conf = str[spos+1:]
print(conf)
conf = float(conf)
print(conf)
print('')


# .replace()
greet = 'Hello Bob'
print(greet)
print('')
nam = input('Enter name: ')
greet = greet.replace('Bob',nam)
print(greet)


