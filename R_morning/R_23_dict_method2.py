#################################################
#  31.07.2023 8.30AM
#################################################
#  TOPICS TO BE COVERED
# 👉 Dictionary Methods
#################################################


# Dictionary is a mutable data type
# Dictionary is ordered

student_info = {
  'samir' : 75,
  'saket' : 74,
  'sanjeev': 81,
  'suresh' : 42
}

# keys() will get all the keys from the dictionary
# values()
# items()


# updating a dictionary
# update({key:value})

print(student_info)

student_info.update({'rakesh': 53})
print(student_info)

student_info.update({'ramesh':47})
print(student_info)

student_info.update({'samir':95})
print(student_info) #existing value belonging to the key will get updated





# setdefault()
# setdefault() = get() + update()


# working as get()
print(student_info.setdefault('suresh'))
print(student_info.setdefault('samir'))
# if the key does not exist , key will be addded by the setdefault method with value as 'None'

print(student_info.setdefault('vikas',88))
print(student_info)

student_info.setdefault('ravi',89)
print(student_info)

# using get() we can inform the user about key
print(student_info.get('rohit','No such Student exists'))
print(student_info.get('samir','No such Student exists'))



# removing items

d6 = {
  'name' : "Ramesh",
  'age' : 24,
  'area' :"Pune",
  'skills' : ['Phy','Chem','Bio',['JS','Python','C++']],
  'hobby' :{'reading','writing'}
}

d6.pop('age')
print(d6)


# d6.remove()
# print(d6)

d6.setdefault('time' ,'Yes')
d6.setdefault('available' ,'Yes')
print(d6)

# will remove the last added item
print(d6.popitem())

d6.setdefault('name' ,'Suresh')
print(d6.popitem())



# Initialising a dictionary
# fromkeys('keys',value)

list_students = ['samir', 'saket', 'sanjeev', 'suresh', 'rakesh', 'ramesh', 'vikas', 'ravi']

print(dict.fromkeys(list_students))
print(dict.fromkeys(list_students,0))
print(dict.fromkeys(list_students,20))

list_val = [10,20,30]
print(dict.fromkeys(list_students,list_val))



list_fruits = ['apple','banana' , 'orange']
print(dict.fromkeys(list_fruits,0))