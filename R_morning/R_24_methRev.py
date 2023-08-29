#Heading One
#Sub Heading one
# Dictionary Methods
d6 = {
  'name' : "Ramesh",
  'age' : 24,
  'area' :"Pune",
  'skills' : ['Phy','Chem','Bio',['JS','Python','C++']],
  'hobby' :{'reading','writing'}
}
print(d6)  #{'name': 'Ramesh', 'age': 24, 'area': 'Pune', 'skills': ['Phy', 'Chem', 'Bio', ['JS', 'Python', 'C++']], 'hobby': {'reading', 'writing'}}


#keys
print(d6.keys())  #dict_keys(['name', 'age', 'area', 'skills', 'hobby'])


#values
print(d6.values())  #dict_values(['Ramesh', 24, 'Pune', ['Phy', 'Chem', 'Bio', ['JS', 'Python', 'C++']], {'reading', 'writing'}])


#items
print(d6.items())  #dict_items([('name', 'Ramesh'), ('age', 24), ('area', 'Pune'), ('skills', ['Phy', 'Chem', 'Bio', ['JS', 'Python', 'C++']]), ('hobby', {'reading', 'writing'})])


#acessing a dict using get()
print(d6.get('age'))  #24

d6.get('skills')  #['Phy', 'Chem', 'Bio', ['JS', 'Python', 'C++']]


d6.get('skills','not available')  #['Phy', 'Chem', 'Bio', ['JS', 'Python', 'C++']]

d6.get('pin','not available') #if the key is not present , the other argument  will be displayed
                              # 'not available'
#update
d6 = {
  'name' : "Ramesh",
  'age' : 24,
  'area' :"Pune",
  'skills' : ['Phy','Chem','Bio',['JS','Python','C++']],
  'hobby' :{'reading','writing'}
}
d6.update({'dob': '12.12.1999'})
 #O/P :# d6
# {'name': 'Ramesh',
#  'age': 24,
#  'area': 'Pune',
#  'skills': ['Phy', 'Chem', 'Bio', ['JS', 'Python', 'C++']],
#  'hobby': {'reading', 'writing'},
#  'dob': '12.12.1999'}


setdefault
d6
#O/p:= {'name': 'Ramesh',
#  'age': 24,
#  'area': 'Pune',
#  'skills': ['Phy', 'Chem', 'Bio', ['JS', 'Python', 'C++']],
#  'hobby': {'reading', 'writing'},
#  'dob': '12.12.1999'}

d6.setdefault('age')
#24

d6.setdefault('hobby')
#{'reading', 'writing'}

d6.setdefault('result2','NO')
#'NO'

d6
#O/p:= {'name': 'Ramesh',
#  'age': 24,
#  'area': 'Pune',
#  'skills': ['Phy', 'Chem', 'Bio', ['JS', 'Python', 'C++']],
#  'hobby': {'reading', 'writing'},
#  'dob': '12.12.1999',
#  'result2': 'NO'}


fromkeys
list_a = ['a', 'b', 'c', 'd']
dict.fromkeys(list_a)
#{'a': None, 'b': None, 'c': None, 'd': None}


dict.fromkeys(list_a, "NA")
#{'a': 'NA', 'b': 'NA', 'c': 'NA', 'd': 'NA'}


dict.fromkeys(list_a, 0)
#{'a': 0, 'b': 0, 'c': 0, 'd': 0}


dict.fromkeys(list_a, [11, 22, 33, 44])
# O/p:={'a': [11, 22, 33, 44],
#  'b': [11, 22, 33, 44],
#  'c': [11, 22, 33, 44],
#  'd': [11, 22, 33, 44]}

