
info = ["shlok","dhokchaule",2,9]
print(type(info)) #<class 'list'>

# program
dictinfo =  {
    "firstName":"manaswi",
    "lastName":"deshmukh",
    "age":3,
    "rollNo":4
}
print(dictinfo) #{'firstName': 'manaswi', 'lastName': 'deshmukh', 'age': 3, 'rollNo': 4}
print(type(dictinfo)) #<class 'dict'>


# program 2

#          0        1       2       3         4
listN = ["apple","mango","banana","grapes","banana"]
print(listN) #['apple', 'mango', 'banana', 'grapes', 'banana']
y1  = len(listN)
print(y1) #5
# list stores the value by index

vehicle = {
    #property:value
    #key:value
    "color":"red",
    "type":"sedane",
    "color":["yellow", "red"]
}
print(vehicle) #{'color': ['yellow', 'red'], 'type': 'sedane'}
# It does not stores value by index

# program 3
animal = {
   "name":"tiger",
    "legs":4,
    "found":["india","bangladesh"]
}
q2 = len(animal)
print(q2) #3


# program 4

k = [11,22,33]
print(k[1]) #22

MH = {
    "city1":"pune",
    "city2":"mumbai"
}
print(MH['city1']) # pune
print(MH['city2']) # mumbai

# add the property to dict
MH['city3'] = "wardha"
print(MH) #{'city1': 'pune', 'city2': 'mumbai', 'city3': 'wardha'}

# update
MH['city2'] = "jaipur"
print(MH) #{'city1': 'pune', 'city2': 'jaipur', 'city3': 'wardha'}

del MH['city3']
print(MH) #{'city1': 'pune', 'city2': 'jaipur'}


# program 5
bank = {
    "accNo":123,
    "bal":10000000000,
    "branch":"khardi",
    "city":"pune"
}

# retrive
print(bank["accNo"]) #123

# add
bank["pincode"] = 411028
print(bank) #{'accNo': 123, 'bal': 10000000000, 'branch': 'khardi', 'city': 'pune', 'pincode': 411028}

# udpate
bank['accNo'] = 456
print(bank)  #{'accNo': 456, 'bal': 10000000000, 'branch': 'khardi', 'city': 'pune', 'pincode': 411028}

# del
del bank['city']
print(bank) # {'accNo': 456, 'bal': 10000000000, 'branch': 'khardi', 'pincode': 411028}

# program 6
fruits = ["apple","mango","banana","papaya"]

for fr in fruits:
    print(fr) # apple  mango  banana  papaya

for fruit in range(len(fruits)):
    print(fruits[fruit]) #apple  mango  banana  papaya