#################################################
#  09.07.2023 9.00AM
#################################################
#  TOPICS TO BE COVERED
# 👉 Strings in Python
# 👉 Negative Indexing
# 👉 Methods in Strings
#################################################

# Negative Indexing

greet =  "WELCOME"
print(greet[-1])
print(greet[-2])


print(greet[0:7:2])
print(greet[0:7:1])
print(greet[::1]) #deafult start and end values


# for string revesal
print(greet[::-1]) #deafult start and end values

# to get the last character in the string
s1 = "We are learning Python v3"
print(s1[24])
print(s1[-1])

s2 = "We are learning Python v4"
print(s2[24])
print(s2[-1])

# how to find the length of the string ??

print(len(s1))
print(len(greet))

# methods are pre written codes
# functions

name = "UmAkAnt"

# name = "Umakant"


# editing related methods

print(name.upper()) #all upper
print(name.lower()) #all lower
print(name.title()) # 1st character of every word in the string


hobby = "to play Football"
print(hobby.title())


print(hobby.casefold()) #???
print(hobby.lower()) # ???

# strip , to remove extra spaces leading and trailing
place  = "       Pune"
print(place)
print(place.strip())


fav = "i Love           Pune"
print(fav.strip())


pin = "          400076         "
print(pin.strip())

# boolean methods
# split
