#  function as an argument
# function in another function
# function as 1st class citizen

x = 100

def func1(a):
    print(2*a)
func1(x)     #200


def greet(name):
    print("Hello ",name)
greet("Akash")    # Hello  Akash


greeting =  greet
greeting("Rakesh")     # Hello  Rakesh


# doc Strings !
def x(a,b,c):
    """
    This function carries out addition of
    three numbers
    user must provide all the three numbers
    else it will give arg missing error
    """
    print(a + b + c)

x(10, 20, 30)      # 60


print(x.__doc__)   #This function carries out addition of three numbers
                    # user  must provide  all the  three numbers
                    # else it  will give  arg  missing  error




def intro(name, age):
    '''
    This function will give the user name and age only
    input name and age only
    age must be in numeric form input
    '''
    print("Myname is {} and my age is {}".format(name, age))
intro('Ramesh', 26)     # Myname is Ramesh and my age is 26


print(intro.__doc__)     #O/P:-  This function  will give the user name and age only
                        # input name and age only
                        # age must be in numeric form input



print(len.__doc__)       # Return the number of items in a container.


print(print.__doc__)       #print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
                            # Prints the values to a stream, or to sys.stdout by default.
                            # Optional keyword arguments:
                            # file: a file - like object(stream); defaults to the current sys.stdout.
                            # sep: string inserted between values, default a space.
                            # end: string appended after the last value, default a newline.
                            # flush: whether to  forcibly flush the stream.



# pep guide 257 : doc string
# https://peps.python.org/pep-0257/

def intro(name, age):
    '''
    This function will give the user name and age only
    input name and age only
    age must be in numeric form input

    '''
    print("Myname is {} and my age is {}".format(name, age))


intro('Ramesh', 26)      # Myname is Ramesh and my age is 26


print(intro.__doc__)      #O/P:-  This function  will give the user name and age only
                            # input name and age only
                            # age must be in numeric form input

