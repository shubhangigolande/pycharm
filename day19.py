

# string as a parameter and string as a return type
def greet(word):
    return  "hello "+ word
q1  = greet("chinmay")
print(q1)

# int as parameter and interger as return type
def calculator(a,b,c):
    print(c)
    return a + b + c
calculator(c = 12, b = 34,a = 56)


# function with default values
def additon(a = 10 , b = 4):
    print(a+b)
additon(100,40)
additon()

# boolean as parameter and boolean as a return type
def canDrive(haveVehicle, age):
    if haveVehicle and age >= 18:
        return True
    else:
        return False
q2 =  canDrive(True , 19)
print(q2)

# list as a parameter and list as a return type
fruits = ["apple","mango"]
def addElement(lisA):
    # lisA = fruits
    lisA.append("banana")
    return lisA
q3 = addElement(fruits)
print(q3)
print(fruits)

# dictionary as a parameter and dictionary as return
info = {
    "firstName":"chinmay",
    "lastName":"deshpande"
}
def addCity(dict):
    dict.update({"city":"pune"})
    return dict
q4 = addCity(info)
print(q4)

# tuple as parameter and tuple as return type
nums = (11,22,33)
def addElementToTuple(tupA):
    tupA = list(tupA)
    tupA.append(14)
    tupA =  tuple(tupA)
    return tupA
q5 = addElementToTuple(nums)
print(q5)


# set as parameter and set as return type

setA = {11,22,33}
setB = {44,55,66}
def addSet(setA,setB):
    return setA.union(setB)
q6 = addSet(setA,setB)
print(q6)

# function as a param and function as return type
# function as a param and function as return type