

# string booelan int float list

listA = ["swara","natasha","rupali","sarika"]
# add
listA.append("khushi")
print(listA) #['swara', 'natasha', 'rupali', 'sarika', 'khushi']
# retrive
print(listA[1]) #natasha
# remove
listA.pop(1)
# update
listA[0] = "manasi"
print(listA) #['manasi', 'rupali', 'sarika', 'khushi']

# program 2
dictB = {
    "firstName":"shivansh",
    "lastName":"golande",
    "age":3
 }
print(type(dictB)) #<class 'dict'>

# retrive
print(dictB['firstName']) #shivansh

# update
dictB['firstName'] = "ansh"
print(dictB) #{'firstName': 'ansh', 'lastName': 'golande', 'age': 3}

# add
dictB['city'] ="baramati"
print(dictB) #{'firstName': 'ansh', 'lastName': 'golande', 'age': 3, 'city': 'baramati'}

# delete
del dictB['lastName']
print(dictB) #{'firstName': 'ansh', 'age': 3, 'city': 'baramati'}


# loop
country  = ["india","pakistan","china","australia","cuba"]

# normal

for city in country:
    print(city) #india  pakistan  china  australia  cuba

for city in range(len(country)):
    print(country[city]) #india  pakistan china australia cuba


# dict

info3 = {
    "fullName":"amol golande",
    "skills":["python","sql"],
    "age":37,
    "city":"pune",
    "canDrive":True,
    "city":"pune"
}

print(info3) #{'fullName': 'amol golande', 'skills': ['python', 'sql'], 'age': 37, 'city': 'pune', 'canDrive': True}
print(info3)  #{'fullName': 'amol golande', 'skills': ['python', 'sql'], 'age': 37, 'city': 'pune', 'canDrive': True}

for prop in  info3:
    print(prop,info3[prop]) #fullName amol golande skills ['python', 'sql']  age 37 city pune canDrive True


l = [11,22,33]
k = l
k[0] = 111
print(k) # [111,22,33]
print(l) # [111,22,33]

vehicle = {
        "color":"purple",
        "city":"mumbai",
        "regNo":123
}
vehicle2  = vehicle
vehicle2['color'] = "blue"
print(vehicle) #{'color': 'blue', 'city': 'mumbai', 'regNo': 123}
print(vehicle2) #{'color': 'blue', 'city': 'mumbai', 'regNo': 123}