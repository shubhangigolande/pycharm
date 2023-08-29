# Positional

def intro(name ,age):
    print("Myname is {} and my age is {}".format(name,age))
intro('Ramesh',26)    #Myname is Ramesh and my age is 26

#
def intro(name ,age):
    print("Myname is {} and my age is {}".format(name,age))
intro(26,'Ramesh')   #Myname is 26 and my age is Ramesh


intro(age=26,name ='Ramesh')   # Myname is Ramesh and my age is 26
intro(name ='Ramesh',age=26,)    #Myname is Ramesh and my age is 26




# **kwars = Dict

def intro(**kwargs):
    for key,value in kwargs.items():
        print(key,value)
intro(name ='Ramesh',age=26)    #name Ramesh  age 26




# **kwars = Dict

def intro(**kwargs):
    for key,value in kwargs.items():
        print(key,value)
intro(name ='Ramesh',age=26,place='Pune',domicile='Punjab',workex=5) #name Ramesh /age 26 /place Pune /domicile Punjab /workex 5


# **vishal = Dict
def intro(**vishal):
    for key,value in vishal.items():
        print(key,value)
intro(name ='Ramesh',age=26,place='Pune',domicile='Punjab',workex=5)  # name Ramesh /age 26 /place Pune /domicile Punjab /workex 5




#lambda Function
# lambda Function
# anonymous function
# nameless
# one line function
def sq(a):
    return a*a
sq(5)     #25



# syntax
# lambda arguments : expresion
lambda a : a*a
#  O/P:-  <function __main__.<lambda>(a)>


sqr =lambda a : a*a
sqr(5)  #25


def cub(x):
    return x*x*x

cub(7)   #343

lambda x : x*x*x
#   O/P:-  <function __main__.<lambda>(x)>

cub = lambda x : x*x*x
cub(7)     #343




# passing the value in the lambda function
# withoust using the name for the nameless function

(lambda x : x*x*x)(7)   #343


print(25)    # 25


(lambda x , y : x+y)(10,20)    # 30


(lambda x , y : x-y)(10,20)   # -10


(lambda x , y : x*y)(10,20)    # 200


(lambda x , y : x/y)(10,20)    # 0.5


(lambda x  : x> 0)(10)     # True


(lambda x  : x> 0)(-10)    # False


(lambda x  : x%2 == 0)(15)     # False


(lambda x  : x%2 == 0)(14)    # True