#################################################
#  05.07.2023 9.00AM
#################################################
#  TOPICS TO BE COVERED
# 👉 Data Types in Python
# 👉 Into to Strings
#################################################





# rules for naming the variable

# allowed

name = "Ramesh"
name1= "Ramesh1"
name2= "Ramesh2"

i_am = "Rakesh"
i_am_ = "Rakesh"
iam_ = "Rakesh"
iam = "Rakesh"
_iam = "Rakesh"
_iam_ = "Rakesh"


# not allowed

# !123 = 123
# $123 = 123
# %123 = 123

# @week = "Sunday"



# allowed but not recommended
# double uderscore dunder variables

__num__ = 500
__dict__ = "total count"
__len__ = 5000
__class__ = "First"
__Shubhangi__= "ONE"


_dipesh = "Dipesh"
__dipesh__ = "Dipesh"


# variable assignment

x = 100

x = 500

x = "Rahul"

x = 5
y = 6
z = 7


# x = 5 , y = 6 , z = 7

a = 100
b = 100
c = 100

a = b = c = 100

print(a)
print(b)
print(c)

#  all variables are using the same value in the backend
# using id()
print(id(a))
print(id(b))
print(id(c))




# Data Types in Python
'''
1. Numbers
    a. Int
    b. Float
    c. Complex
2. Strings
3. List
4. Tuples
5. Sets
6. Dictionaries
7. Boolean
8. etc etc..
'''

# Intro to strings Data type

fruit =  "Banana"
type(fruit)
print(type(fruit))

x = 10
print(type(x))

pi = 3.1417
print(type(pi))
