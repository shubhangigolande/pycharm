# Fixed  lenght  parameters

def calc(a, b):
    print(a + b)   #136
    print(a - b)   #-10

calc(63, 73)



# Variable lenght parameters


def sum(*args):
    sum = 0
    for i in args:
        sum = sum + i
    print(sum)     # 30
    print(args)   #(10, 20)
    print(type(args))   #<class 'tuple'>
sum(10, 20)




#  * indiacates variable legth

def sum(*args):
    sum = 0
    for i in args:
        sum = sum + i
    print(sum)     #120
    print(args)    #(10, 11, 11, 22, 66)
    print(type(args))    #<class 'tuple'>

sum(10, 11, 11, 22, 66)



#  * indiacates variable legth
#  args is not compulsory
#  its a industry practice


def sum(*kajal):
    sum = 0
    for i in kajal:
        sum = sum + i
    print(sum)    #120
    print(kajal)    #(10, 11, 11, 22, 66)
    print(type(kajal))   #<class 'tuple'>
sum(10, 11, 11, 22, 66)





# Types of argumnets
# Positional


def intro(name, age):
    print("Myname is {} and my age is {}".format(name, age))

intro('Ramesh', 26)    #Myname is Ramesh and my age is 26


intro(26,'ramesh')     #Myname is 26 and my age is ramesh




# Default

def greet(city="Our city"):
    print('welcome to : ', city)      #welcome to :  Pune
greet("Pune")

greet()     #welcome to :  Our city




#  variable lenght argument
# **kwargs
def func1(a,b,c=0,*args):
    print(a)
    print(b)
    print(c)
func1(10, 20, 100)     #10   #20    #100

func1(100, 200)    #100     #200    #0




def func1(c=0, a, b, *args):
    print(a)
    print(b)
    print(c)

# o/p:=Input In[28]
# def func1(c=0, a, b, *args):
#     ^
#     SyntaxError: non - default argument follows default argument




    def func1(*args, a, b, c=0):
        print(a)
        print(b)
        print(c)

    func1(10, 20)
    # O/P:=---------------------------------------------------------------------------
    # TypeError Traceback(most recent call last)
    # Input In[30], in < cell  line: 1 > ()
    # ----> 1   func1(10, 20)

    # TypeError: func1() missing   2    required  keyword - onlyarguments: 'a' and 'b'



    # positional , default , *args , **kwargs
    def calc1(*args):
        print(args)

    calc1(10)    # (10,)
    calc1(10, 20, 30)      #(10, 20, 30)

