# 8 Sep, 24
"""
Topics Covered:
+ Comments
+ Escape Sequences
+ Variables
+ Data Types
"""

# It is Single line comment.
"""
This is
multiple line
comment.
"""
# We can use single quote and double quote too inside print function
print("NED UNIVERSITY")
print('NED UNIVERSITY')

### Excape Sequences ###

# print('It's a cat.') --> wrong that's why showing error
print('It\'s a cat') # correct way is to use \ with '

print("My name is Noor. \nMy age is 21.") # Breaking each sentence in New line

### Variable ###

# Syntax --> variable_name = "value"

name = "Noor"
roll_no = 22

# How to print value of variable using variable name
print(name) # It will print value (Noor) stored in variable (name)

### Data Types ###

"""
1. Numeric
2. Text (String)
3. Boolean (bool) means True or False
"""

# Numeric (Integer, Float, Complex)

age = 21 # integer (int) means whole numbers
cgpa = 3.4 # float means include decimal 
# We will study complex type in next class 

# Text (String)

course_name = "Python for Absolute Beginners"

# Boolean

a = 4
b = 6
c = a < b # Since a is less than b, so it'll print True, so the type of this variable / data is boolean
print(c) 

# How to find tyoe of variable
print(type(c))
