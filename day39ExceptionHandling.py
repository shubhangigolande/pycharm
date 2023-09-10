# Program 1

# a=100
# b=0
# c=a/b
# print(c)
            # O/P;- Traceback (most recent call last):
            #   File "C:\Users\Amol\PycharmProjects\pythonProject\venv\src\day39ExceptionHandling.py", line 5, in <module>
            #     c=a/b
            #       ~^~
            # ZeroDivisionError: division by zero


# program 2

# name="MINSKOLE"
# print(name[7])
# print(name[17])
# O/P :-   #Traceback (most recent call last):
            #   File "C:\Users\Amol\PycharmProjects\pythonProject\venv\src\day39ExceptionHandling.py", line 15, in <module>
            #     print(name[17])
            #           ~~~~^^^^
            # IndexError: string index out of range
            # E


#program 3
# a=100
# try:
#     b=input("enter a number")
#     c=a/b
#     print(c)
# except:
# O/P:- #Enter a NUmber0
        # Some error occured





#program 4

# a=100
# try:
#     b=input("enter a number")
#     print(type(b))
#     c=a/b
#     print(c)
# except:
#     print("some error occured")
# O/P:-     #enter a number10
            # <class 'str'>
            # some error occured




# program 5
# a=100
# try:
#     b=int(input("enter a number"))
#     print(type(b))
#     c=a/b
#     print(c)
# except:
#     print("some error occured")
    #O/P :-     #enter a number100
                # <class 'int'>
                # 1.0




# USING Else in try .....except
#program 6
# a = 100
# try:
#     b = int(input("Enter a NUmber"))
#     print(type(b))
#     c = a / b
#     print(c)
#
# except Exception as error:
#     print("Some error occured", error)
# else:  # this will be exceuted if there is no exception
#     print("Code executed successfully , congrats !!! ")
#O/P:-  #Enter a NUmber100
        # <class 'int'>
        # 1.0
        # Code executed successfully , congrats !!!



#USING FINALLY
#program 7
# a = 100
# try:
#
#     b = int(input("Enter a NUmber"))
#     print(type(b))
#     c = a / b
#     print(c)
#
# except Exception as error:
#     print("Some error occured", error)
# else:  # this will be exceuted if there is no exception
#     print("Code executed successfully , congrats !!! ")
# finally:  # always get executed
#     print("This code will always get executed , irrespective of the execution status under try..except block")
#O/P:-      #Enter a NUmber00
            # <class 'int'>
            # Some error occured division by zero
            # This code will always get executed , irrespective of the execution status under try..except block



# CUSTOM Exception
#program 8
# x =  int(input("Enter a number"))
# print(x)
#O/P:-      #Enter a number100
            # 100


#program 8
# x =  int(input("Enter even  number only "))
# print(x)
#O/P:-      #Enter even  number only 23
            # 23


#program 9
## creating user defined Exception !!!
# x =  int(input("Enter even  number only "))
# if x%2 !=0:
#     raise Exception("ONly even numbers are allowed")
# else:
#     print(x)
#O/P:-      #Enter even  number only 23
            # Traceback (most recent call last):
            #   File "C:\Users\Amol\PycharmProjects\pythonProject\venv\src\day39ExceptionHandling.py", line 136, in <module>
            #     raise Exception("ONly even numbers are allowed")
            # Exception: ONly even numbers are allowed



# HANDELLING USER DEFINED Exception
#program 10
## creating user defined Exception !!!
# try:
#     x =  int(input("Enter even  number only "))
#     if x%2 !=0:
#         raise Exception("ONly even numbers are allowed")
#     else:
#         print(x)
# except:
#     print("Only even number allowed")
#O/P:-      #Enter even  number only 23
            # Only even number allowed





#program 11
# def cal_age(year_born):
#     current_year = 2023
#     age = current_year - year_born
#     print(age)
# cal_age(2000)
# O/P:- 23




#program 12
# def cal_age(year_born):
#     current_year = 2023
#     age = current_year - year_born
#     print(age)
# cal_age(2030)
# O/P:-   #-7



#program 13
# def cal_age(year_born):
#     current_year = 2023
#     if current_year<year_born:
#         raise Exception("Invalid  year of birth")
#     else:
#         age = current_year - year_born
#         print(age)
# cal_age(2030)
#O/P:-      #Traceback (most recent call last):
            #   File "C:\Users\Amol\PycharmProjects\pythonProject\venv\src\day39ExceptionHandling.py", line 194, in <module>
            #     cal_age(2030)
            #   File "C:\Users\Amol\PycharmProjects\pythonProject\venv\src\day39ExceptionHandling.py", line 190, in cal_age
            #     raise Exception("Invalid  year of birth")
            # Exception: Invalid  year of birth




#program 14
def cal_age(year_born):
    current_year = 2023
    if current_year < year_born:
        raise Exception("Invalid  year of birth")
    else:
        age = current_year - year_born
        print(age)


try:
    cal_age(2090)
except:
    print("Invalid  year of birth")
# O/P:-     #Invalid  year of birth


# Syntax error
# Exception
#     Built in exception : class : Exception
#     User defined  :  using "raise" keyword

# try:
#     code that is prone to error
# except Exception/precise sub-class as error (https://docs.python.org/3/library/exceptions.html#exception-hierarchy)
#     print custom msg
# else :
#    if the code exceuted without any exception
# finally :
#    in all situation
