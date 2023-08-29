
# Lamba

def add(x,y):
    print(x+y)
add(12,3)


# lamda arguments : expression
x = lambda a:a+10
print(x(3))


# program 2
y = lambda a,b: a*b
a = y(13,2)
print(a)

# program 3
z = lambda a,b,c:a+b+c
print(z(12,3,4))

# program 4
def myfunc():
    return lambda a,b:a*b
x = myfunc()
#x = lambda a,b:a*b
print(x(12,4))


#program5
x = lambda a,b:a+b
def myFunc2(n):
    #n = lambda a,b:a+b
    print(n(12,4))
myFunc2(x)

# program 6

num = [1,2,3,4,5,6,7,8,9,10]
#[2,4,6,8,10,12,14,16,18,20]
tn = []
for x in num:
    #print(x*2)
    tn.append(x*2)
print(tn)

q1 = list(map(lambda x :x*2,num))
print(q1)


# program 2
listB = [24,5,6,7,8,4,55,66,7]
above10 = []
for x in listB:
    if( x > 10):
        above10.append(x)
print(above10)

listC = list(filter(lambda x : x > 10,listB))
print(listC)#