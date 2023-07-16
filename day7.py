
#            0       1       2        3
fruits = ["apple","mango","banana","orange"]
print(fruits[0])
print(fruits[2])

# slice
#        0        1           2        3         4
city = ["pune","banglore","kolkata","nagpur","chennai"]
#         -5     -4          -3           -2        -1

# program 2
#city[startIndex:endIndex:steps]
print(city[1:])
print(city[-3:])
print(city[0:4])
print(city[1:4])
print(city[-4:4])
print(city[1:-1])
print(city[-1:-4])
print(city[0:len(city):2])
print(city[0:len(city):3])

# program 3

vegtables = ["cabbage", "cauliflower","potato","brinjal"]
print("cabbage" in vegtables)
#
# q1 = input("please enter the vegetable you wish to buy\n")
# if(q1 in vegtables):
#     print('vegetable available')
# else:
#     print('vegetable not available')

# program 4
vegtables = ["cabbage", "cauliflower","potato","brinjal"]

for vegetable in vegtables:
    print(vegetable)

fruits = ["apple","mango","bananan","grapes"]

for  fruit in fruits:
    print(fruit)

# program 5
#
# for x in range(startIndex,endIndex,step):
#     print(x)
#

for x in range(10):
    print(x)

for x in range(1,10):
    print(x)

for x in range(2,22,2):
    print(x)

#           0       1        2         3
fruits = ["apple","mango","bananan","grapes"]
for x in range(len(fruits)):
    #print(x)
    print(fruits[x])
