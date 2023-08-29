

# SET
# set does not stores the value

q1 =  {11,22,33,44,55,66,77,88,99,100,100}
print(q1)
print(type(q1))

# Set does not stores the value by index and does not to store duplicate values
# retrive
for item in q1:
    print(item)

print(111 in q1)

# update -- NO

# add()
cities = {"pune","mumbai","banglore","kolkata","nagpur"}
print(cities)
q3 = cities.add("nanded")
print(cities)
print(q3)

# update()
cities.update({"bhopal","delhi","indore","ludhiana"})
print(cities)

#remove()
cities.remove("indore")
print(cities)
#cities.remove("nashik")

#discard()
cities.discard("bhopal")
print(cities)

#pop()
cities.pop()
print(cities)

#clear()
cities.clear()
print(cities)

#del cities
print(cities)