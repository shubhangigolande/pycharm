
place = "pune"
print(place)
print(place[0])


# program 2
city1 = "chandrapur"
#0    1    2   3   4  5   6  7  8 9
# c   h    a   n   d  r  a  p   u  r

# program 3

city3 = 'mumbai'
city4 = """ hi """
city5 = ''' pune'''

print(city3)
print(city4)
print(city5)
print(type(city3))

# Type
# Properties and Methods
# Methods -- action and return


animal = "tiger"
q3 = len(animal)
print(q3)

# program 4
# upper
q4 = animal.upper()
print(q4)

# program 4

city5 = "LUCKNOW"
q5 = city5.lower()
print(q5)

# program 5
q6 = city5.count("K")
print(q6)

#program 6
q7 = city5.startswith("LUCK")
print(q7)

#program 7
q8 = city5.endswith("nOW")
print(q8)

#program 8
#chainable
q9 = "ansh".lower().upper()
print(q9)

#program 9
#strip := strip methods are removed start and ends spaces

q10 = "  banana  "
print(len(q10))

q9 = q10.strip()
print(q9)
print(len(q9))

# program 10
# split :=splits methods are cut the string small chunks
info = "shubhangi amol golande"
q10 = info.split(" ")
# ["shubhangi","amol","golande"]
print(q10)


# program 11
email = "shubhangigolande26@gmail.com"
ss = email.split('@')
# ['shubhangi', 'amol', 'golande']
print(type(ss))
print(ss)
#['shubhangigolande26', 'gmail.com']

# program 12
#Return a copy with all occurrences of substring old replaced by new
var1 = "I am learning javascript"
aa = var1.replace("javascript","python")
print(aa)

# program 13
mks = "12"
q13 = mks.isdigit()
print(q13)


# program 14
mks2 = "adasdsa"
q14 = mks2.isalpha()
print(q14)

marks="bhxgcvgx21"
gg=marks.isalpha()
print(gg)

# program 15
marks4 = "A213213 "
q15 = marks4.isalnum()
print(q15)

#program 16

citys = " goa "
# print(len(citys))
# q1 = citys.strip()
# print(len(q1))

# program 17
citys1 = " Bhopal"
q2 = citys1.lstrip()
print(len(q2))

# program 18
citys5 = " wardha "
print(len(citys5))
q3 = citys5.rstrip()
print(len(q3))

# program 19
info = "I am  learning js "
q4 = info.title()
print(q4)

# program 20
city10 = "pune is nice place to leave"
q5 = city10.capitalize()
print(q5)

# program 21
city11 = "NaGpur"
q6 = city11.swapcase()
print(q6)

# program 22

city13 = "jaipur"

# 0     1    2    3    4   5
# j     a    i    p    u   r
q7 = city13.index("a")
print(q7)

# 0  1  2  3  4  5  6  7  8  9 10 11 12
# c  h  a  n  d  r  a  p  u  r  a  e  a

city14 = "chandrapuraea"
q8 = city14.index("a",5)
print(q8)

q9 = city14.index("a",7,11)
print(q9)

first_name = "shubhangi"
lastName = "bhosale"
print("My firstname is {} and lastName is {}".format(first_name,lastName))


# ----------------------------------------------------------------


# 'in' keyword

fruits = "apple mango banana chikoo papaya kiwi orange"
if "kiwi" in fruits:
    print("fruit is available")
else:
    print("fruit is not available")



# program 1
def printName(fn,ln):
    print("My firstName is {} and my lastName is {}".format(fn,ln))

printName("sarika","kokane")
printName("rupali","deshmukh")

