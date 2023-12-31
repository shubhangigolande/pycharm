#################################################
#  14.07.2023 9.00AM
#################################################
#  TOPICS TO BE COVERED
# 👉 Lists in Python
# 👉 Lists Methods
#################################################

# for editing the list

# append
list_fruits = ['apple','mango','guava','chiku']
print(list_fruits)
print(list_fruits.append("banana"))
print(list_fruits) #in-places changes took place

# in-places changes : original list will be affected
# temporary changes


# insert
list_num = [11,22,33,44,55,66] #add 35 :  33 ?  44
# list_num.append(35)
# print(list_num)
list_num.insert(3,35) #in-places changes
print(list_num)

# extend

list_veg  = ['potato','onion','brinja']
list_veg.extend(list_fruits)
print(list_veg)


# sort

list_alpa = ['q', 'w', 'e', 'r', 't', 'u', 'y']
print(list_alpa.sort()) #in-places changes
print(list_alpa)


list_num = [44,55,77,11,44,88,9]
list_num.sort()
print(list_num)


list_alnum = ['a','f',45,'g',44]
# list_alnum.sort()  #TypeError
print(list_alnum) #'int' and 'str'


list_alnum = ['a','f','45','g','44']
list_alnum.sort()  # ? basis of sorting : HW
print(list_alnum) #'int' and 'str'


# list_num = [44,55,77,11,44,88,9,[1,2,3]]
# list_num.sort() #not supported
# print(list_num)


# reverse
#  index position

list_num = [44,55,66,11,22,33]
list_num.reverse()
print(list_num)


list_alnum = ['a','f',45,'g',44]
list_alnum.reverse()
print(list_alnum)
