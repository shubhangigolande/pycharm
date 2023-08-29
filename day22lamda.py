# square of a numbers
# program 1
q = lambda x: x * x
print(q(2))

# addition of two numbers
# program 2
q2 = lambda  x,y : x + y
print(q2(12,3))

# greatest of two element
# program 3
q3 = lambda  x , y  : x if x > y else y
print(q3(1,3))

# program 4 - as a return type
def  myFun():
    return  lambda x:x * 10
q1 = myFun()
#q1 = lambda x:x * 10
print(q1(2))

# program 5   -- as a parameter
q2 = lambda a,b:a+b
print(q2(12,4))
def addition(fn):
    #fn = lambda a,b:a+b
    print(fn(23,4))
addition(q2)







# javascript
# let a = 10
# let b = 5
# let q = a > b ? a : b
#
# int h = 10
# int q = 5
# int grt = h > q ? h : q
#
# h = 10
# q = 5
# print(h if h > q else q)