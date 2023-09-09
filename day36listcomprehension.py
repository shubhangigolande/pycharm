#
# # program 1    square of numbers
numbers=[1,2,3,4,5,6,7,8,9]
newlist=[]
for i in numbers:
    newlist.append(i*i)
print(newlist)

# Syntax
# # [expression for item in iterable if condition]
square=[i * i for i in numbers ]
print(square)

# #program 2
names=['amol','anil','ansh','shivansh','niketan','nikhil','ram','sai']
Unames=[item.upper() for item in names]
print(Unames)


# #program3
nameU=[item.upper() for item in names if len(item)>=5]
print(nameU)


# #program 4    series  1 -10
series=[i for i in range(1,11)]
print(series)

#table of numbers
tbl=[i * i for i in range(1,11)]
print(tbl)

# #program 5
students=[
    {'firstname':'shubhangi','age':33},
    {'firstname':'jagruti','age':29},
    {'firstname':'rupali','age':32}
]
q1=[sname for sname in students if sname['age']>30]
print(q1)


# q5 = [student for student in students if student['age'] >= 30 and student['fullName'].startswith("k")]
# print(q5)
#
# #program 6
#
# birthYear = [2001,1999,1998,1999,2000]
# q6 = [2023 - year for year in birthYear ]
# print(q6)
#
# q7 = list(map(lambda year:2023 - year,birthYear))
# print(q7)
#
#
# q8 = list(filter(lambda student:student['age'] >= 30,students))
# print(q8)

# list comprehension
#[1,2,3]
# a=[2,4,6,8]
# b=0
# for i in a :
#     b=b+i
# print(b)

totalsum=sum([i for i in range(1,11)])
print(totalsum)

# reduce

from functools import reduce
sum=reduce(lambda x,y : x+y, range(1,11))
print(sum)

