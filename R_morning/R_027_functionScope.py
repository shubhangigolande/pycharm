# Scope  of  Variable


def banner():
    x = 100
    print(x)


banner()  # 100
banner()  # 100
banner()  # 100

# pro 2
x = 10
def banner():
    x = 100  # local scope
    print(x)

banner()  # 100


#pro 3
# if the value is not in the local scope, fun will search in the Global space
x = 10  # global Scope

def banner():
 x = 100 #local scope
print(x)
banner()  # 10


#pro 4
# the fuction can modify the local variable only
# global variable will not be modified
x = 10
def banner():
    x = 5
    x = x ** 2
    print(x)
banner()   # 25


#pro 5
# the fuction can modify the local variable only
# global variable will not be modified even if it is refenced inside the fun
x = 10


def banner():
    #     x = 5
    x = x ** 2
    print(x)

banner()
------------------------
#  O/p:= UnboundLocalError                         Traceback (most recent call last)
# Input In [7], in <cell line: 9>()
#       6     x = x**2
#       7     print(x)
# ----> 9 banner()
#
# Input In [7], in banner()
#       4 def banner():
#       5 #     x = 5
# ----> 6     x = x**2
#       7     print(x)
#
# UnboundLocalError: local variable 'x' referenced before assignment



# the fuction can modify the local variable only
# global variable will not be modified even if it is refenced inside the fun
x = 10
def banner():
#     x = 5
    global x
    x = x**2
    print(x)   #10

print(x)  #100
banner() #this has changed the global value of x
print(x)   #100


# the fuction can modify the local variable only
# global variable will not be modified even if it is refenced inside the fun
x = 10
def banner():
    x = 5
    global x
    x = x**2
    print(x)

print(x)
banner() #this has changed the global value of x
print(x)
# O/p:=   Input In [9]
#     global x
#     ^
# SyntaxError: name 'x' is assigned to before global declaration





# the fuction can modify the local variable only
# global variable will not be modified even if it is refenced inside the fun
x = 10
def banner():
    global x
    x = 5
#     x = x**2
    print(x)   #10

print(x)   # 5
banner() #this has changed the global value of x
print(x)  #5



# use  of global is not recommneded
name = "Suresh"

def change_name():
    global name
    name = "Ramesh"
    print(name)     #Suresh

print(name)    #Ramesh
change_name()
print(name)     #Ramesh



