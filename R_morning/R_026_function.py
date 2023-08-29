#Classification of Functions
# built in
# user defined
# recursion
# lambda
#image.png

# based on Partameters
# based on return values
#image.png


# without parameters
# behaves like static function
# not much use
# dummy functions
def star():
    print("***************")


star()   #  ** ** ** ** ** ** ** *

star()   #  ** ** ** ** ** ** ** *

# with parameters
# function not returning value
def adder(a, b):
    print(a + b)


adder(75, 85)  # 160


# function not returning value
def adder(a, b):
    #     print(a+b)
    return (a + b)


ans = adder(75, 85)
print(ans * 2) # 320

# role of return in function


def salry(x, y):
    return x + y


total = salry(100, 5)
print(total * 2)  #210


def salry(x, y):
    return x + y
    print("salary for jan 2025")  # this will be ignored

total = salry(100, 5)
print(total * 2)   # 210


# no code will be executed after the return line
def salry(x, y):
    return x + y  # 1st return statement will be considered
    return x - y  # this will be ignored

total = salry(100, 5)
print(total * 2)  # 210


def salry(x, y):
    return x + y, x - y

total = salry(100, 5)
print(total)  #(105, 95)
print(total * 2)  # (105, 95, 105, 95)
print(type(total))  #<class 'tuple'>



# default values


def calc(a, b, c):
    print(a + b + c)


    calc(10,20,30)  #60


# required sum of two numbers only

def calc(a, b, c):
    print(a + b + c)


calc(10, 20, 0)  # 30


# required sum of two numbers only

def calc(a, b, c=0):
    print(a + b + c)


calc(10, 20) #30   # default value of c will be used in the additon



# required sum of two numbers only

def calc(a, b, c=0):
    print(a + b + c)

calc(10, 20, 100)   #  130


# required sum of two numbers only

def calc(a=0, b=0, c=0):
    print(a + b + c)


calc(10)    # 10


# required sum of two numbers only

def calc(a=0, b=0, c=0):
    print(a + b + c)


calc()    #0


def greet():
    print("Welcome to Pune")


greet()     # Welcome to Pune


def greet(city):
    print("Welcome to ", city)


greet('Pune')    #  Welcome to Pune


def greet(city):
    print("Welcome to ", city)


greet('nagpur')    # Welcome to nagpur


def greet(city="Our City"):
    print("Welcome to ", city)


greet()    # Welcome to Our City
