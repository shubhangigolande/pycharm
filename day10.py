# info={
#         "firstname":"shubhangi",
#         "lastname":"golande",
#         "rollno":3,
#         "city":"pune"
# }
# print(info) #{'firstname': 'shubhangi', 'lastname': 'golande', 'rollno': 3, 'city': 'pune'}
# print(type(info)) #<class 'dict'>
#
# info2=info
# print(info2) #{'firstname': 'shubhangi', 'lastname': 'golande', 'rollno': 3, 'city': 'pune'}
#
# info2["firstname"]="minal"
# print((info)) #{'firstname': 'minal', 'lastname': 'golande', 'rollno': 3, 'city': 'pune'}
# print(info2) #{'firstname': 'minal', 'lastname': 'golande', 'rollno': 3, 'city': 'pune'}
#
# x=123
# vehicle={
#         "color":"red",
#         "type":"seddane",
#         "regno":x
# }
# print(vehicle) #{'color': 'red', 'type': 'seddane', 'regno': 123}
# vehicle2=vehicle.copy()
# vehicle2['color']="blue"
# print(vehicle) #{'color': 'red', 'type': 'seddane', 'regno': 123}
# print(vehicle2) #{'color': 'blue', 'type': 'seddane', 'regno': 123}
#
# vehicle2['regno']=456
# print(vehicle2) #{'color': 'blue', 'type': 'seddane', 'regno': 456}
#
# # program 3
#
#
# vehicle={
#         "color":"red",
#         "type":"sadane",
#         "regno":123
# }
# vehicle.pop('regno')
# print(vehicle) #{'color': 'red', 'type': 'sadane'}
#
#
# # program 5
# b=vehicle2.get('type')
# print(b) #seddane
#
# b = vehicle2.get('Type')
# print(b) #None
# # #print(vehicle2['Type'])


# program 6


info3 = {
        "firstName":"shubhangi",
        "lastName":"golande",
        "age":23,
        "rollNo":45
}

for x in info3:
       print(x,info3[x]) #firstName shubhangi lastName golande age 23 rollNo 45

for x in info3:
        print(info3[x]) #shubhangi golande 23 45

for prop in info3.keys():
        print(prop) #firstName lastName age rollNo


for val in info3.values():
        print(val) #shubhangi golande 23 45


for item in info3.items():
        print(item) #('firstName', 'shubhangi') ('lastName', 'golande') ('age', 23) ('rollNo', 45)

# info3.clear()
# print(info3) #('rollNo', 45)
#
# # fromkeys()
# x = ("name","age","rollNo")
# y = None
# q1 = dict.fromkeys(x,y)
# print(q1) #{'name': None, 'age': None, 'rollNo': None}
#
# # update()
# q1.update({"name":"shubhangi"})
# q1.update({"lang":"hindi"})
# print(q1) ##{'name': 'shubhangi', 'age': None, 'rollNo': None, 'lang': 'hindi'}
#
#
# info3 = {
#         "language":"hindi",
#         "city":"pune",
#         "country":"India"
# }
#
# #print(info3.popitem()) #('country', 'India')
#
# info3.popitem()
# print(info3) #{'language': 'hindi', 'city': 'pune'}
#
# q1 = info3.setdefault("language",None)
# print(q1) #hindi