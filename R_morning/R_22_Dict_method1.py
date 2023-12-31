#################################################
#  29.07.2023 8.30AM
#################################################
#  TOPICS TO BE COVERED
# 👉 Dictionary in Python
#################################################

#

student_info = {
  'samir' : 75,
  'saket' : 74,
  'sanjeev': 81,
  'suresh' : 42
}

# key: value > item

# key ?
#  keys work like index
# key should be unchangeable data type , i.e hashable
# value can be any data type allowed in Python



d1 = {
  'a' : 100,
  'b' : 200,
  'c' : 300
}

print(d1)

d2 = {
  500 : 100,
  600 : 200,
  700 : 300
}
print(d2)

# d3 = {
#   [11,22] : 100,
#   [22,33] : 200,
#   [33,44] : 300
# }
# print(d3) #unhashable type: 'list'










d3 = {
  (11,22) : 100,
  (22,33) : 200,
  (33,44) : 300
}
print(d3)#hashable type: 'tuple'


# d3 = {
#   {11,22} : 100,
#   {22,33} : 200,
#   {33,44} : 300
# }
# print(d3)#unhashable  type: 'set'


d6 = {
  'name' : "Ramesh",
  'age' : 24,
  'area' :"Pune",
  'skills' : ['Phy','Chem','Bio',['JS','Python','C++']]
}


print(d6)

print(d6['skills'])
print(type(d6['skills']))

print(d6['skills'][0])
print(d6['skills'][2])
print(d6['skills'][3][1])


# creating a dict using other data types
# using constructor

x = 2
y = 5
z = 7


# using values
d7 = dict(x = 2,y = 5,z = 7)
print(d7)
print(d7['x'])
print(d7['y'])


list_com = ['x','y','z']
list_off = [2,5,7]

# using lists
# using zip methods
d8  = dict(zip(list_com,list_off))
print(d8)

# using pair of  tuple
# dict([tuple pairs])

d9 = dict([('x',2),('y',5),('z',7)])
print(d9)

# methods in dictionary

# to access the dictionary

d6 = {
  'name' : "Ramesh",
  'age' : 24,
  'area' :"Pune",
  'skills' : ['Phy','Chem','Bio',['JS','Python','C++']]
}
# get() to access the values

print(d6.get('age'))
print(d6.get('area'))
print(d6.get('skills')[0])

# keys() will get all the keys from the dictionary
# values()
# items()

print(d6.keys())
print(type(d6.keys()))

print(d6.values())
print(type(d6.values()))


print(d6.items()) #o/p will be a list having tuple pairs
print(type(d6.items())) #o/p will be a list having tuple pairs)


d6 = {
  'name' : "Ramesh",
  'age' : 24,
  'area' :"Pune",
  'skills' : ['Phy','Chem','Bio',['JS','Python','C++']],
  'hobby' :{'reading','writing'}
}
print(d6)


#  dictionary : indexing ? are dictionary ordered ?





d6 = {
  'name' : "Ramesh",
  'age' : 24,
  'area' :"Pune",
  'skills' : ['Phy','Chem','Bio',['JS','Python','C++']]
}
print(d6)
print(d6.keys())
print(d6.values())
print(d6.items())