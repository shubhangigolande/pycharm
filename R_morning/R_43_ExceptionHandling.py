a = 100
b = 200
c = 0

print(a / b)        #0.5
print(a / c)
#O/P:----------------------------------------------------------------------------
# ZeroDivisionError      Traceback(most recent call last)
# Input In[8], in < cell line: 6 > ()
# 3 c = 0
# 5 print(a / b)
# ----> 6 print(a / c)
#
# ZeroDivisionError: division by zero

# Error eg:SyntaxError
# Exception eg:ZeroDivisionError








a = 100
b = 200
c = 0

print(a / b)       #0.5
print(a / c)
print("this line is very imp, should always be printed")
# O/P:----------------------------------------------------------------------------
# ZeroDivisionError       Traceback(most recent call last)
# Input In[10], in < cell line: 6 > ()
# 3 c = 0
# 5 print(a / b)
# ----> 6 print(a / c)
# 7 print("this line is very imp, should always be printed")
#
# ZeroDivisionError: division by zero





# try:
# # the code where chances of exception is there
# #     code1
# #     code2
# except:
# # msg if the exception occurs

# implementing the Exception handeling
a = 100
b = 200
c = int(input("Please Enter a number!!!"))  # type casting

print(a / b)
try:
    print(c)
    print(type(c))
    print(a / c)

except:
    print("There is some error")

print("this line is very imp, should always be printed")

# Input In[23]
# except:
# ^
# IndentationError: expected an indented block after  'try' statement on line 1









# implementing the Exception handeling
a = 100
b = 200

print(a / b)
try:
    c = int(input("Please Enter a number!!!"))
    print(c)
    print(type(c))
    print(a / c)
except:
    print("There is some error")

print("this line is very imp, should always be printed")

#O/P:-
# 0.5
# Please Enter  a number!!!potato
# There is some error
# this line is very imp, should always be printed









# implementing the Exception handeling
# sending proper msg to the user
a = 100
b = 200

print(a / b)
try:
    c = int(input("Please Enter a number!!!"))
    print(c)
    print(type(c))
    print(a / c)
except:
    print("There is some error,check the entered number , should not be zero")

print("this line is very imp, should always be printed")
#O/P:-
# 0.5
# Please Enter a number!!!potato
# There is some error, check the entered number, should not be zero
# this line is very imp, should always  be printed





name = "SURESH"
print(name)
print(name[0])
print(name[10])
print("this line is very imp, should always be printed")
# O/P:=
# SURESH
# S
# ---------------------------------------------------------------------------
# IndexError                  Traceback(most recent call last)
# Input In[27], in < cell line: 4 > ()
# 2 print(name)
# 3 print(name[0])
# ----> 4 print(name[10])
# IndexError: string index out of range






name = "SURESH"
print(name)
print(name[0])
try:
    a = int(input("Enter the index post to be printed!!"))
    print(name[a])
except:
    print("Index out of range, user proper range ")
print("this line is very imp, should always be printed")
#O/P:-
# SURESH
# S
# Enter  the index post to be printed!!6
# Index out of range, user proper range
# this line is very imp, should always be printed







name = "SURESH"
print(name)
print(name[0])
try:
    a = int(input("Enter the index post to be printed!!"))
    print(name[a])
except Exception as i:
    print(i)  # the error msg given by python
print("this line is very imp, should always be printed")
#O/P:-
# SURESH
# S
# Enter the index post to  be printed!!8
# string index out of  range
# this line is very imp, should always be printed







# implementing the Exception handeling
# sending proper msg to the user
a = 100
b = 200

print(a / b)
try:
    c = int(input("Please Enter a number!!!"))
    print(c)
    print(type(c))
    print(a / c)
except Exception as e:
    print(e, "Enter a non zero number")

print("this line is very imp, should always be printed")
#O/P:-
# 0.5
# Please Enter a number!!!0
# 0
# < class 'int'>
# division by zero Enter a non zero number
# this line is very imp, shouldn always be printed

# https://docs.python.org/3/library/exceptions.html






# implementing the Exception handeling
# sending proper msg to the user
a = 100
b = 200

print(a / b)
try:
    c = int(input("Please Enter a number!!!"))
    print(c)
    print(type(c))
    print(a / c)
except Exception:  # not necessary ??
    print("Enter a non zero number")

print("this line is very imp, should always be printed")
#O/P:-
# 0.5
# Please Enter a number!!!potato
# Enter a non zero number
# this line is very imp, should always be printed
