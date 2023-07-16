fruits=["sai","shiv","ganesh","nikhil","sameer"]

marks = [22,33,44,55,85,77]
info = ["shubhangi","golande",33,True]

z = "chinmay"
print(type(z))
print(type(info))


# program 1
# Types ---->
# Properties and methods
#               0         1          2           3
vegetables = ["carrot","brinjal","cauliflower","cabbage"]
print(vegetables[0])
print(vegetables[3])
q1 = len(vegetables)
print(q1)


# program2

# Method - Gym()
# Action  --- Excercise
# Return  --- Health

vegetables = ["carrot","brinjal","cauliflower","cabbage"]
q2 = vegetables.append("ladyfinger")
print(q2)
print(vegetables)


# program 3
vegetables = ["carrot","brinjal","cauliflower","cabbage","carrot"]
q3 = vegetables.count("carrot")
q4 = vegetables.count("Carrot")
print(q3)
print(q4)

# program 4
#               0        1            2           3        4
vegetables = ["carrot","brinjal","cauliflower","cabbage","carrot"]
q5 = vegetables.index("carrot",1)
q6 = vegetables.index("cabbage",1,4)
#q7= vegetables.index("brinjal",2,4)
print(q5)
print(q6)
#print(q7)

# program 5
#          0          1       2        3        4        5
fruits = ["apple","banana","orange","grapes","chikoo","papaya"]
# q8 = fruits.pop()
# print(fruits)
# print(q8)

q9 = fruits.pop(4)
print(q9)
print(fruits)



