# revision


# using try...except block to cathc the exception


a = 100
name  = "MAYUR"

try:
    b = int(input("ENter a number other than zero")) #there is a possibility that user might enter the valuse as '0'
    c = a/b
    print(c)
    print(name[1])
except:
    print("Some error occured") #printing some genereic info only

#O/p:-
# ENter a number other than zero4
# 25.0
# A





a = 100
name  = "MAYUR"

try:
    b = int(input("ENter a number other than zero"))
    c = a/b
    print(c)
    print(name[1])
except Exception as e: # prnting specific exception using the Built in excepton
    print(e)
#O/P:- ENter a number other than zero0
# division by zero




a = 100
name  = "MAYUR"

try:
    b = int(input("ENter a number other than zero"))
    c = a/b
    print(c)
    p = int(input("ENter the index position to be called"))#there is a possibility that user might enter the valuse beyond the available index position
    print(name[p])
except Exception as e: ## prnting specific exception using the Built in excepton
    print(e)
#O/P:-  ENter a number other than zero0
# division by zero




a = 100
name  = "MAYUR"

try:
    b = int(input("ENter a number other than zero"))
    c = a/b
    print(c)
    p = int(input("ENter the index position to be called"))
    print(name[p])
except Exception as e: #this will catch the exception
    print(e)
#O/P:-
# ENter a number other than zero0
# division by zero




a = 100
name  = "MAYUR"

try:
    b = int(input("ENter a number other than zero"))
    c = a/b
    print(c)
    p = int(input("ENter the index position to be called"))
    print(name[p])
except Exception as e:
    print(e)
#O/P:-
# ENter a number other than zero9
# 11.11111111111111
# ENter the index position to be called10000
# string index out of range




# Handeling each type of exception using their specific class
# thus the code will be better

a = 100
name  = "MAYUR"

try:
    b = int(input("ENter a number other than zero"))
    c = a/b
    print(c)
    p = int(input("ENter the index position to be called"))
    print(name[p])
except ZeroDivisionError as e:
    print(e)
except IndexError as f:
    print(f)
#O/P:-
# ENter a number other than zero10
# 10.0
# ENter the index position to be called4
# R


# if the code executed without any excepitions we can inform the same using 'else' block

# else block will be executed only if none of the Exception blocks are called

a = 100
name = "MAYUR"

try:
    b = int(input("ENter a number other than zero"))
    c = a / b
    print(c)
    p = int(input("ENter the index position to be called"))
    print(name[p])
except ZeroDivisionError as e:
    print(e)
except IndexError as f:
    print(f)
else:  # this will get executed only if the code was without any excception
    print("All codes executed successfully")
# a = 100/0

# O/P:-
# ENter a number other than zero5
# 20.0
# ENter the index position to be called2
# Y
# All  codes executed successfully


# irrespective of the code execution status 'finally' block will be executed


a = 100
name = "MAYUR"

try:
    b = int(input("ENter a number other than zero"))
    c = a / b
    print(c)
    p = int(input("ENter the index position to be called"))
    print(name[p])
except ZeroDivisionError as e:
    print(e)
except IndexError as f:
    print(f)
else:  # this will get executed only if the code was without any excception
    print("All codes executed successfully")
finally:
    print("This will always be executed, irrespective of code status")
# a = 100/0

#O/P:-
# ENter a number other than zero0
# division by zero
# This will always be executed, irrespective of code status



# User defined Exception
# raising the user defined exception

x = int(input("enter an Even number"))
if x%2!=0:
    raise Exception("Enter Even numbers only")
else:
    print("Entered number is Even")
#O/P:- enter an Even number3
# ---------------------------------------------------------------------------
# Exception                                 Traceback (most recent call last)
# Input In [39], in <cell line: 4>()
#       3 x = int(input("enter an Even number"))
#       4 if x%2!=0:
# ----> 5     raise Exception("Enter Even numbers only")
#       6 else:
#       7     print("Entered number is Even")
#
# Exception: Enter Even numbers only




# raising the user defined exception
# handeling the exception

def calculate_age(year_born):
    current_year = 2023
    if year_born>current_year:
        raise Exception("Invalid year of birth")
    else:
        age = current_year -year_born
        print(age)

try:
    calculate_age(2030)
except:
    print("Invalid year of birth, enter proper year")

print("This is imp")
#O/P:-
# Invalid year of birth, enter proper year
# This is imp

