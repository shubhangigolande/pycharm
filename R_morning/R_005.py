#################################################
#  08.07.2023 9.00AM
#################################################
#  TOPICS TO BE COVERED
# 👉 Strings in Python
# 👉 Indexing
# 👉 Slicing
#################################################

# Indexing
#         0123456
greet =  "WELCOME"
print(greet)
print(type(greet))

print(greet[0])
print(greet[5])
print(greet[4])

#    012345
s = "It's a nice day"
print(s[2])
print(s[5])
print(s[4])


# Slicing
#         0123456
greet =  "WELCOME"

# var_name[start:end] wil go for n-1
print(greet[0:2])
print(greet[0:3]) # WEL

# COME

print(greet[3:7])
print(greet[3:]) #default last element will be considered
print(greet[:7]) #default first element will be considered



# Slicing with JUMP Values
# var_name[start:end:JUMP] wil go for n-1

#         0123456
greet =  "WELCOME"


print(greet[0:7:1]) # zero skipped
print(greet[0:7:2]) #one skipped WLOE

print(greet[::2]) #one skipped WLOE
print(greet[::3]) #one skipped WCE



# negative Indexing
print(greet[-2])


# HW

'''
1. w = "+911234567890"
> use slicing to get below O/P
+91
89
+

2. r = "We are learning Python v3.8"
v3.8

Python

3. d = "1 2 3 4 5"
print with skip/jump value 2

'''
