#################################################
#  25.07.2023 8.30AM
#################################################
#  TOPICS TO BE COVERED
# 👉 for loop
# 👉 range()
#################################################

# for loop in strings


# Syntax
# for i in iterable:
#   code


name = "MINSKOLE"

print(name)
print(name[0])
print(name[1])

for i in name:
    print(i)

num = 123456789

# for i in num: #'int' object is not iterable
#   print(i)


num = "123456789"
for i in num:  # 'int' object is not iterable
    print(i, type(i))

tup_fruits = ('apple', 'banana', 'orange')
print(tup_fruits[0])

for i in tup_fruits:
    print(i)

# understanding range()
# to generate list of numbers
# last element is not included

# range()


print(0)
print(1)
print(2)
print(3)
print(4)
print(5)

# data type vs function

print(range(0, 10))
print(type(range(0, 10)))
print(list(range(0, 10)))

# range(start,end)
print(list(range(0, 10)))  ## last element is not included
print(list(range(0, 11)))  ## last element is not included

print(list(range(11)))  # default start value is 0

# range(start,end,step size)
print(list(range(0, 11, 2)))  # even number
print(list(range(1, 11, 2)))  # odd number

# print table of 5


print(list(range(5, 51, 5)))

# print table of 7

print(list(range(7, 71, 7)))

# negative values
print(list(range(0, -10)))  # []
print(list(range(-10, 0)))  #
print(list(range(-10, 0, 2)))  #
print(list(range(-10, 0, -2)))  # []

# step size has to be an integer
# decimal/flaot as step size is not allowed in range()

# print(list(range(7,71,0.5)))