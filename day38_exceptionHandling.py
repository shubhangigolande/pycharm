# Exception Handling
# Program 1
print("hello")

a=100
b=200
c=0
c=a/b
print("Bye")
print(c)
print("Hello")


# program 2
#             0          1        2       3
# names=["shubhangi","sahil","pragati","rahul"]
# print("hello")
# print(names[4])     #O/P:-    #File "C:\Users\Amol\PycharmProjects\pythonProject\venv\src\day38_exceptionHandling.py", line 15
# #     0          1        2       3
# # IndentationError: unexpected indent
# print("bye")

# Combination 1
# try :
#      # statement
#
# except:
#     # statements


#combination  2

# try :
#     # statement
# except:
#     #statement
# else:
#     statement


#try
    #statement
#except
    #statement
#else:
    #statement
#finally
    #statement


# program 1 #try & except
print("hello")
try:
    a = 100
    b = 200
    b = 0
    c = a / b
except:
    print("something went wrong") # generic message
print("Bye")
print("hello2")


# # program 2   #try except exception as error
print("hello");
try:
    s=100
    t=0
    print(s/t)
except Exception as error:
    print(error)
print("bye")


# program 3
print("hello")
try:
    names = ["apple","banana","mango"]
    print(names[4])
except Exception as error:
    print(error)
print("bye")


# program 4
print("hello")
try:
    names = ["sparrow","duck","crow"]
    a = 10
    b = 20
    print(a/b)
    print(names[2])
    # print(z)
except ZeroDivisionError as e:
    print(e)
    print("please enter correct input")
except IndexError as e:
    print(e)
    print("you list does not contain that much element")

