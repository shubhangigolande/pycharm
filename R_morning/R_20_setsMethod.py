#################################################
#  27.07.2023 8.30AM
#################################################
#  TOPICS TO BE COVERED
# 👉 Set
# 👉 Set Methods
#################################################

# Set in Python
# set is an unorderd collection *** of unique object ****
# indexing cant be used to acce the elements inside a set
# duplicates are not allowed
# unhashable i.e can be changed
# empty set is a dictionary


# Editing a set

set_num = {2,4,6,8,10}
set_num.add(12)
print(set_num)

set_fruits = {'apple','mango','banana'}
set_fruits.add('kiwi')
print(set_fruits)

set_fruits.add(93)
print(set_fruits)

set_fruits.add('apple')
print(set_fruits)#o/p will contain unique values


# set operations
set_e = {0,2,4,6,8,10}
set_o = {0,1,3,5,7,9}

print(set_e.union(set_o))
print(set_o.intersection(set_e))
print(set_o.difference_update(set_e))
print(set_o.difference(set_e))

# membership in sets
# boolean outputs

set_1 = {1,2,3,4,5,6,7,8,9}
set_2 = {2,4,6,8}
set_3 = {0}



print(set_2.issubset(set_1))
print(set_1.issubset(set_2))
print(set_1.issuperset(set_2))

print(set_1.isdisjoint(set_2))
print(set_2.isdisjoint(set_1))

print(set_2.isdisjoint(set_3))
print(set_3.isdisjoint(set_1))


# removing items from a set
# pop
# pop will change the original set

set_1 = {0,1,2,3,4,5,6,7,8,9}
print(set_1.pop()) #removes randomly one element from the set
print(set_1.pop()) #removes randomly one element from the set
print(set_1.pop()) #removes randomly one element from the set
print(set_1.pop()) #removes randomly one element from the set
print(set_1.pop()) #removes randomly one element from the set
print(set_1)

# remove
set_1 = {0,1,2,3,4,5,6,7,8,9}
set_1.remove(9)
print(set_1)


set_1.remove(0)
print(set_1)

# set_1.remove(0)
# print(set_1)





set_1 = {1,2,3,4,5,6,7,8,9}
set_2 = {2,4,6,8}
set_3 = {0}
print(set_2.issubset(set_1))


if set_3.issubset(set_1):
  print("set 2 is Subset of set 1")
else:
  print("Not a subset ")