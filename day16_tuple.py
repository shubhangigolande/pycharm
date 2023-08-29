
fruit = ["apple","mango", "banana"]
print(fruit)
print(type(fruit))

fruit = ("apple","mango","banana")
print(fruit)
print(type(fruit))

# tuple stores the value by index
print(fruit[0])
#fruit[0] = "chikoo"
print(fruit)


fruit  = list(fruit)
fruit[1] = "chikoo"
fruit = tuple(fruit)
print(fruit)

fruit  = list(fruit)
fruit.append("banana")
fruit = tuple(fruit)
print(fruit)


# range
#           0         1        2         3
names  = ("mayuri","poorva","abhisha","shraddha")
#           -4         -3          -2         -1
print(names[:3])
print(names[1:])
print(names[1:3])
print(names[-4:-1])
print(names[-1:-4])
print(names[1:-1])

#           0         1         2        3
names  = ("mayuri","poorva","abhisha","shraddha")

for item in names:
    print(item)

for item in range(len(names)):
    print(names[item])

names = list(names)
names.remove("poorva")
print(names)
names = tuple(names)
print(names)

#del names


j = 10
print(j)
print(type(j))

j  = 10,
print(type(j))


# unpacking
cities = ("pune","banglore","kolkalata","chennai")
a = cities[0]
b = cities[1]
c = cities[2]
d = cities[3]
print(a,b,c,d)

#(x1,x2,x3,x4) = cities
#(x1,x2,*x3) = cities
#print(x1,x2,x3,x4)

tupleD = (11,22,33)
tupleC = (44,55,66)

tupleE  = tupleD + tupleC
print(tupleE)

t = tupleE * 2
print(t)

country = ("india","srilanka",'pakistan',"japan","india")
q = country.count("india")
print(q)

w = country.index("india",1)
print(w)



rev = ""
first_Name = "chinmay"
for item in range(len(first_Name)):
    rev = first_Name[item] + rev
print(rev)