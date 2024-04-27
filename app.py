import math

print("Hello World")
print("fuck u " * 10)
var = 'fuck u butthead'
print(var)

# Function to get length of string
course = " Python Programming "
# calling the function and entering course as the argument/parameter
print(len(course))
print(course[0])  # getting the character at index 0 from course string
print(course[-1])  # last character of string
# slicing/returning the characters in a range of index, the last index is not inluded.
print(course[0:3])
print(course[0:])  # new string thats the same as original string
print(course[:3])  # python will default to 0:3
print(course[:])  # copy of original string

print(course.upper())  # turns string to uppercase
print(course.lower())  # turns string to lowercase
print(course.capitalize())  # caps the first letter in the string
print(course.title())  # caps the first letter in every word
print(course.strip())  # removes white spaces
print(course.rstrip())  # removes right end white spaces
print(course.lstrip())  # removes left end white spaces
# find index of a character or sequence of characters in a string
print(course.find("Pro"))
# replace all of a character or sequence of characters with something else
print(course.replace("P", "j"))
# check for the existence of a character or sequence of character in a string
print("Pro" in course)
# check if a character or sequence of character in a string does not exist
print("dsfdr" not in course)

# numbers
print(10 + 3)
print(10 - 3)
print(10 / 3)  # division returns a float
print(10 // 3)  # returns an integer when divided
print(10 % 3)  # modulius -> remainder of a division
print(10 ** 3)  # exponent -> a num to the power of another num

x = 10
x += 3  # augmented assignment operator
print(x)

# useful functions to work with numbers
print(round(2.9))  # rounds a num
print(abs(-2.9))  # returns absolute value of a num

# if you want to use complex mathemtaical calculations, you need to use a math module
# import the module at top of file -> import math
print(math.ceil(2.2))  # return the ceiling of a number

# type conversions
x = input("x: ")  # getting and storing user input in a variable named x

# how to convert a string to a num
int(x)
float(x)
# return the type of a variable
print(type(x))
y = int(x) + 1
print(y)
