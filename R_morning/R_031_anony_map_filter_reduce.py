# syntax
# lambda arguments : expresion
# A lambda function in Python is a small, anonymous, and inline function that can have
# any number of arguments
# but can only have one expression.
# It is also sometimes referred to as a "lambda expression" or "lambda notation."
# Lambda functions are often used for short, simple operations that can be defined in a single line of code.


def nume(num):
    if num%2==0:
        print("number is even")
    else:
        print("Number is odd")
nume(23)      #Number is odd

nume(24)    #number is even




nume_lam  = lambda num : "Even Number" if num%2==0 else

nume_lam(23)    # 'Odd Number'

nume_lam(1999)     #'Odd Number'




# map()
# The map() function in Python is a built-in function that takes in two or more arguments:
#     a function and one or more iterable objects (like lists, tuples, etc.).
# It applies the given function to each item in the iterables and returns an iterator that yields the results
# The basic syntax of the map() function is as follows:
# map(function, iterable1, iterable2, ...)

list_num = [10, 45, 78, 78, 99, 58, 44, 12, 89]
list_num2 = [11, 22, 33, 44, 55]

def doublenum(arjun):
    ans = []
    for i in arjun:
        ans.append(i * 2)
    print(ans)

doublenum(list_num)      #[20, 90, 156, 156, 198, 116, 88, 24, 178]
doublenum(list_num2)


list(map(lambda x: x * 2, list_num))       #[20, 90, 156, 156, 198, 116, 88, 24, 178]
list(map(lambda x: x * 3, list_num))       # [30, 135, 234, 234, 297, 174, 132, 36, 267]



filter()
list_score = [11, 44, 77, 88, 44, 11, 22, 55, 66]

def even_num(x):
    ans = []
    for i in x:
        if i % 2 == 0:
            ans.append(i)
    print(ans)

even_num(list_score)     #[44, 88, 44, 22, 66]




# filter(function,iterable)
def even_ans(x):
    if x % 2 == 0:
        return x


#filter(even_ans, list_score)    # filter at  0x218d36f54e0 >


list(filter(even_ans, list_score))
[44, 88, 44, 22, 66]
