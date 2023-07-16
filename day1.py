#program 1

print('hello')

a=100
print(a)

a=400
print(a)

#program 2
#Arithmetic operation
#addition       +
#substraction   -
#division       /
#multiplication *
#modulus        %


z=10
y=5

print(z+y)
print(z-y)
print(z/y)
print(z*y)
print(z%y)

print(36% 5)

q = 8
r = 4

print(q+r)
print(q-r)
print(q*r)
print(q/r)
print(q%r)

# DRY ----- Don't repeat yourself
# 10 pair --- 50 lines
def calci(x,y):
    print(x+y)
    print(x + y)
    print(x - y)
    print(x * y)
    print(x / y)
    print(x % y)
calci(12,8)
calci(54,7)
calci(45,6)




# function without parameter and without return type

def addiA():
    print(78+98)
addiA()
addiA()
addiA()

# function with parameter and without return type
def addiB(s,v):
    print(s+v)
addiB(12,8)
addiB(75,6)


# function with parameter and with return type
def addiC(d,w):
    return d+w
w1=addiC(54,6)
print(w1)
print(w1+75)
print(w1*5)
print(w1/3)
print(w1-2)
print(w1*0.5)


def Subs(x,y):
    return x*y
r1=Subs(10,5)
print(r1)


def multi(a,b):
    return a*b
a1=multi(r1,2)
print(a1)

