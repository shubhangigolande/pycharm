#Intro to Function
# why do we need a function
a = 100
b = 200
c = a + b
print(c)
#300
a = 1000
b = 2000
c = a + b
print(c)
#3000

# DRY
# Do not Repeat Yourself
#Types of functions
# Types of functions
# inbuild functions
# https://docs.python.org/3.10/library/functions.html
image.png

#custom / user defined
print("***************")  #***************

print("***************")  #***************


print("***************")   #***************


print("***************")  #***************

# how to define a functions

# def name_of_func():
#     code
def star():
    print("***************")

    # how to use a function
    # 1. define a fuction
    # 2. call a function
    star
   # < function__main__.star() >
    star()  #    ** ** ** ** ** ** ** *

    star()   #    ** ** ** ** ** ** ** *

    star()    #    ** ** ** ** ** ** ** *


    # we can call a function any number of times
    # adding two numbers

    # a = 100
    # b = 200
    # c = a + b
    # print(c)

    def adder(a, b):
        print(a + b)

    adder(100, 200)   #    300

    adder(71, 75)   #    146


    # HW
    # 1. write a function to multiply three integers
    # 2. write a function to divide two numbers
    # 3. write a function to make the string UPPER case
