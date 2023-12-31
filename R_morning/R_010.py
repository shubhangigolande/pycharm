#################################################
#  13.07.2023 9.00AM
#################################################
#  TOPICS TO BE COVERED
# 👉 Lists in Python
#################################################


# revision

#  using []
num_even = [2,4,6,8,10]

# using constructor | fancy name for  a function


name  =  "MINSKOLE"
print(list(name))
print(list("MINSKOLE"))

print(type(num_even))



# accessing elements/objetc/items inside a list


# Accessing a list
#                   0       1       2      3        4
#                  -5       -4      -3     -2      -1
students_name = ['Amar','Akash','Anuj','Amit','Anik']

print(students_name[2])
print(students_name[-3])

print(students_name[0])
print(students_name[4])


# Slicing a list

print(students_name[0:3])
print(students_name[:3])
print(students_name[2:5])
print(students_name[2:])

# with step value
# print(students_name[strt:stop:step])
print(students_name[0:5:1])
print(students_name[0:5:2])
print(students_name[::2])

#  use of neg indexing
print(students_name[::-1]) #list reversal


list_one = ["1" , "0" , " " , "5"]
print(list_one[2])



#  accessing a nested list
#             0   1   2   3 4 [0   1   2    3   4]
list_alpa = ['b','c','d','f',['a','e','i','o','u']]

print(list_alpa)
print(type(list_alpa))

print(list_alpa[1])
print(list_alpa[3])
print(list_alpa[4])
print(list_alpa[4][2])

list_alpa = ['b','c','d','f',['a','e','i','o','u',[11,22]]]


print(list_alpa[4][5][1])
