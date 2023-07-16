# program 1
fruits = ["apple","mango","banana"]
fruits.append("chikoo")
print(fruits)

# program 2
# clear
fruits.clear()
print(fruits)

# program3

fruits = ["apple","mango","banana"]
breakfast = fruits
breakfast[0] = "papaya"
print(fruits)
print(breakfast)


# program 4
numbers = [11,22,33]
numsB =  numbers.copy()
numsB[1] = 88
print(numsB)
print(numbers)

# program 5
numberH = [22,33,44,55,22,33,44,55]
q1 = numberH.count(22)
print(q1)

# program 6
city = ["pune","banglore","kolkata"]
city2 = ["nagpur","wardha","akola"]
city2.extend(city)
print(city2)

# program 7
q1 = city.index("pune")
print(q1)

# program 8
country = ["india","srilanka","pakistan"]
country.insert(2,"cuba")
print(country)

#program 9
q2 = country.pop()
print(q2)

#program 10
country.remove("india")
print(country)

#program11
veg = ["tomato","potata","brinjal"]
veg.reverse()
print(veg)

# program 12
names = ["ram","sham","chinmay","poorva","sarika"]
names.sort()
print(names)