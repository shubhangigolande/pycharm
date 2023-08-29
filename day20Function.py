# functions
# def - keyword
# add - function name
# x,y  - parameter
# return - keyword
# q1 - variable
# 12,34 - arguments

def add(x,z):
    return x+z
q1 = add(12,13)
print(q1)

# program 2
def addB(x = 1  ,y = 3 ,z = 4):
    return x + y + z
addB(13,4)
addB()
addB(12)

# program 3
def addC(y,x,z):
    print(x/2)
addC(x = 8 ,y = 90 , z = 20)

# program 4
def addD(x1,x2,x3,x4,x5):
    print(x1+x2+x3+x4+x5)
addD(1,3,4,5,6)

# program 5
def addD(*nums):
    print(nums)
    sum = 0
    for a in nums:
        sum = sum + a
    return sum

q4 = addD(1,2,3,4,5)
print(q4)

# tupA  = (11,22,33)
# sum = 0
#
# for i in tupA:
#     sum = sum + i
# #          0  + 11  =====> 11
# #          11 + 22  =====> 33
# #          33 +  33 =====> 66
# print(sum)

# program 6
def childName(**names):
    print(names)
    for prop in names:
        print(prop ,names[prop])
childName(firstName = "chinmay",lastName = "deshpande",middleName = "shirish")