# 15 September, 24

# Complex data type
z = 4 + 3j
print(z)
print(type(z)) # The type is complex

print(z.real) # 4.0 is real 
print(z.imag) # 3 is imaginary

# How to change data type in variables --> TYPE CASTING

# int to str
x = str(5)
print(type(x))

# str to int
y = int("3")
print(type(y))

# float to int
z = int(4.2)
print(type(z))

# int to float
a = float(1)
print(type(a))

# str to float
b = float("4")
print(type(b))

# float to str 
c = str(22.2)
print(type(c))

# Input and Output
name = input("Enter your name:") # Enter a value --> Input function input()
print(name) # Output function --> print()

age = input("Enter your age:")
print(age)

# OPERATORS --> used to perform any operations on values or variables

# Arithmetic Operators
"""
+ , - , / , * , % , ** , //
"""

# Add
d = 12
e = 5
print(d+e)
f = d + e
print("Sum of d and e is:", f)

# Subtraction
s = 12
t = 4
u = s-t
print("Answer of subtraction is:", u)

# Division
print(d / e) # 12 / 5 --> 2.4

# Floor division
print(d // e) # whole number 

# Multiplication
print(d * e) # Output 60

# Exponent
m = 3 # base
n = 4 # exponent 
print(m ** n) # 3*3*3*3 = 81 

# Modulus --> operator %; will give us the remainder after division
print(d % e) # 12/5 --> 2 is remainder 

# Practice Program

num1 = int(input("Enter number 1 to add:")) # Taking input
num2 = int(input("Enter number 2 to add:")) # Taking input
sum = num1 + num2 # Adding using arithmetic operators
print("Sum of number 1 and 2 is:", sum) # Output

# Assignment Operator --> to assign values
"""
= , += , -= , /= , *=
"""
i = 5 # here assignment operator is = 
age1 = 4 
# age2 = age1 + 5; output --> age1 + 5 = 9
age1 += 5 # here assignment operator is += --> output is age1 + 5 = 9; but short way
print(age1)


