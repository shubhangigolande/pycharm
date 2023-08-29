# Program 1

fruits = ["apple","mango","banana","grapes"]
print(type(fruits))
print(fruits)
fruits[3] = "papaya"


fruitsB = ("apple","mango","banana")
print(fruitsB)
print(type(fruitsB))

# tuples stores the value by index
# tuples does not support item assignment
# tuple is  fixed  length
# tuple can store duplicate values
#                0         1           2           3         4
vegetables = ("brinjal","carrot","cauliflower","cabbage","cabbage")
print(vegetables[0])
print(vegetables[1])


# Error
# vegetables[1] = "ladyfinger"
# print(vegetables)
print(vegetables)


canDrive = (True , False ,False ,True)
numberTuple = (11,22,33,44,55)
listTuple = ([11,22],[22,33],[44,55])
dictTuple = (
    {"firstName":"chinmay","lastName":"deshpande"},
    {"firstName":"sarika", "lastName":"pansare"}
)

# Program 2
#            0          1           2        3        4
country = ("india","pakistan","srilanka", "canada" ,"usa")
#            -5       -4       -3            -2      -1
print(country[1])
print(country[-1])

# tupleName[startIndex:endIndex (not inclusive)]
print(country[1:])
print(country[:4])
print(country[1:4])
print(country[-4:4])
print(country[0:-1])

print("india" in country)
print("India" not in country)
if("india" in country):
    print("name exist")
else:
    print("does not exist")


# update
flowers = ("lotus","rose","lily","sunflower")
#flowers[1] = "jasmine"
flowers = list(flowers)
print(flowers)
flowers[1] = "jasmine"
print(flowers)
flowers = tuple(flowers)
print(flowers)


tupleA = (11,22)
tupleB = (33,44)
tupleC = tupleA + tupleB
print(tupleC)

tupleD = tupleA * 2
print(tupleD)

# remove item
#          0   1    2    3
state = ("MH","MP","UP","RJ")
print(state)
state = list(state)
print(state)
state.remove("MP")
print(state)
state = tuple(state)
print(state)

print(len(state))

# deleting the tuple
del state


# program 3 unpackng

tupleA = ("ram","sham","ganesh")

a = tupleA[0]
print(a)
b = tupleA[1]
print(b)
c = tupleA[2]
print(c)

(x1,x2,x3) = tupleA
print(x1)
print(x2)
print(x3)


colors = ("red","black","green","blue")
(c1,c2,*c3) = colors
print(c1)
print(c2)
print(c3)


# loop
#           0     1       2      3
colors = ("red","black","green","blue")
for item in colors:
    print(item)

for item in range(len(colors)):
    #print(item)
    print(colors[item])


#method
#           0      1      2       3      4
colors = ("red","black","green","blue","red")
x1 = colors.count("red")
print(x1)

x2 = colors.index("black")
print(x2)