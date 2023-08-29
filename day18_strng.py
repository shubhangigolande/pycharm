s = 10
t = 5

print(s+t)
print(s-t)
print(s*t)
print(s/t)
print(s%t)

a = 8
b = 4

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)

# string as a parameter and string as return
def greet(word):
    print("welcome "+ word)
    return "welcome "+word
q1  = greet("chinmay")
print(q1)

# boolean as a parameter and boolean as return type
def canDrive(age ,vehicleAvailable):
    if(vehicleAvailable and age >= 18):
        return  True
    else:
        return False

q2  = canDrive(17,True)
print(q2)

# list as parameter and list as return type
fruits = ["apple","mango","banana"]
def removeApple(lst):
    # lst = fruits
    lst.remove('apple')
    return lst
q3 = removeApple(fruits)
print(q3)
print(fruits)

# dictionary as parameter and dictionary as return type

info = {
    "firstName":"chinmay",
    "lastName":"deshpande",
    "age":23,
    "rollNo":34
}

def addCity(dict):
    cityAdd = {"city":"pune"}
    dict.update(cityAdd)
    return dict
q4  = addCity(info)
print(q4)

# tuple as a parameter and tuple as return type

numbers = (11,22,33)
def addValue(tupA):
    # tuple is converted to list
    tupA = list(tupA)
    # add the element to list
    tupA.append(13)
    # convert list to tuple
    tupA = tuple(tupA)
    # return tuple from addValue function
    return tupA
q5 = addValue(numbers)
# q5 is tuple return from addValue function
print(q5)

# set as a parameter and set as return type
setA = {11,22,33}
setB = {33,44,55}

def ComBine(setA,setB):
    return setA.union(setB)
setE = ComBine(setA,setB)
print(setE)