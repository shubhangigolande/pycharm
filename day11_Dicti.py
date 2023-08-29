
info = {
    "firstName":"chinmay",
    "lastName":"deshpande",
    "age":23,
    "rollNo":56,
    "age":34
}
print(info)
for prop in info:
    print(prop,info[prop])

# retrive
print(info['firstName'])
# update
info['firstName'] = "tanmay"
# add
info['city'] = "pune"
# del
del info['age']

info2 = {
    "firstName":"chinmay",
    "lastName":"deshpande",
    "age":23,
    "rollNo":56,
    "age":34
}

#get()
q1 = info2.get('firstkame')
# print(info2['FirstName'])
print(q1)

# clear()
# q2 = info2.clear()
# print(info2)
# print(q2)

#popitem()
info2.popitem()
print(info2)

#pop()
info2.pop('firstName')
print(info2)

vehicle = {
    'color':"black",
    "type":"sedane"
}
# print(vehicle)
# vehicle2 = vehicle
# vehicle2['color'] = "blue"
# print(vehicle)
# print(vehicle2)

vehicle2 = vehicle.copy()
vehicle2['color'] = "red"
print(vehicle)
print(vehicle2)

vehicle = {
    'color':"black",
    "type":"sedane",
    "regNo":123,
    "chaseNo":889
}

#Update()
vehicle.update({"city":"pune","wheels":4})
print(vehicle)


#keys()
for prop in vehicle.keys():
    print(prop)


# values()
for val in vehicle.values():
    print(val)


# items()
for item in vehicle.items():
    print(item)

# fromkeys()
q3 = dict.fromkeys(("fn","ln","rn"),None)
print(q3)

# setdefault()
q4 = vehicle.setdefault("chaseNo","786")
print(q4)

