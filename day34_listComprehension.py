# list comprehension
# program 1
vegi=['brinjal','cabbage','tomato','potato','cauliflower']
newlist=[]

for item in vegi:
    newlist.append(item)
print (newlist)

# [expression  for item in list if condition]

# program 2

num=[1,2,3,4,5,6,7,8,9,10]
num2=[]

for item in num:
    num2.append(item * item)
print(num2)
# or   # # [expression for item in list if condition]
square= [item*item for item in num]
print (square)



# program 3
# # [expression for item in list if condition]
birthyear =[1990,1991,1992,1993,1994,1995]
currentyear=[2023- item for item in birthyear]
print (currentyear)



# # program 4
cities=['baramati','pune','nagpur','sangamner','daund']
c1=[item.upper() for item in cities]
print(c1)


# #program 5
gnames=['swara','kirti','sanu','samiksha','girija','garima','sai']
q1=[item.upper() for item in gnames if len(item)>=5]
print(q1)


# # program 6
num =[11,222,43,45,68,4,55,45,71,35,66]
s1=[item for item in num if item % 2 ==0]
print(s1)

numm =[11,22,33,44,22,44,12,14,16,18,20]
s11=[item for item in numm if item % 2 ==0]
print(s11)


# # program 7
d2="maharashtra"
# d2={
#     "m":1,
#     "a":4,
#     "h":2,
#     "r":2,
#     "s":1,
#     "t":1
# }
dictA={}
for char in d2:
    dictA[char]=dictA.get(char,0)+1
print(dictA)



# e.g:-
info  = {
    "firstName":"shubhangi",
    "lastName":"golande"
}

print(info['firstName'])
info.get('firstName')
info['age'] = info.get('age',33)
print(info)