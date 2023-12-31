#################################################
#  11.07.2023 9.00AM
#################################################
#  TOPICS TO BE COVERED
# 👉 Strings in Python
# 👉 String Formatting
# 👉 Escape sequence
#################################################

print("Hello World")

print("C:\logs")

# print("C:\Users\Public\Libraries") #unicode error



# ESCAPE SEQUENCE


# Escape Character Meaning
# \”                Double quote
# \’                Single quote
# \\                backslash
# \n                New line
# \r                Carriage Return
# \t                Horizontal tab
# \b                Backspace
# \f                form feed
# \v                vertical tab
# \0                Null character
# \N{name}          Unicode Character Database named Lookup
# \uxxxxxxxx        Unicode Character with 16-bit hex value XXXX
# \Uxxxxxxxx        Unicode Character with 32-bit hex value XXXXXXXX
# \ooo              Character with octal value OOO
# \xhh              Character with hex value HH

# using escape Character \


print("C:\\Users\Public\Libraries")
print("C:\\Users\Public\Libraries\\tanmay")


# using r-string i.e raw string

print(r"C:\Users\Public\Libraries")
print(r"C:\Users\Public\Libraries\tanmay")
print(R"C:\Users\Public\Libraries\tanmay")


# use of escape SEQUENCE

print("Ramesh,Rakesh,Ujjwal")
print("Ramesh")
print("Rakesh")
print("Ujjwal")


print("Ramesh,\nRakesh,\nUjjwal")
print("Ramesh,\tRakesh,\tUjjwal")


#string formatting
name = "Shital"
place = "Nagpur"
skill =  "Python"

print("I am Shital from Pune with Python Skills")
print("I am name from place with Python skill")
print("I am", name , "from", place, "with", skill, "Skill")



print("I am {} from {} with {} skill".format(name,place,skill))
print("I am {0} from {1} with {2} skill".format(name,place,skill))
print("I am {2} from {1} with {0} skill".format(name,place,skill))
print("I am {0} from {0} with {0} skill".format(name,place,skill))





# using f-string

print("I am {name} from {place} with {skill} skill")
print(f"I am {name} from {place} with {skill} skill")


# HW
'''
A. use .format() to print below statement using the numerical values stored in variables

a = 100
b = 200
c = 300

The price of coke is 300 , spice is 100 and vcr is 200

Shyam has scored 300 in science , 200 in Physics and 300 in Maths


B. use f-string to print  below statement using the numerical values stored in above variables

The price of coke is 300 , spice is 100 and vcr is 200

Sameer has scored 300 in science , 200 in Physics and 300 in Maths


'''
a = 100
b = 200
c = 300

print("The price of coke is {} , spice is {} and vcr is {}".format(c,a,b))
print("The price of coke is {2} , spice is {0} and vcr is {1}".format(a,b,c))
