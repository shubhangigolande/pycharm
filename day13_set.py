# set
setA  = { 11,22,33,44,55,66,11,22,33,44}
print(type(setA))

# does stores the value by index
# sets are not ordered
# set does not stores the value in (key-value pair format)


# retrive
for x in setA:
    print(x)


# add
print("------------------------")
setB = {"chinmay","despande",34,55.6,True}
q1 = setB.add("pune")
print(q1)
print(setB)
print("chinmay" in  setB)

if "chinmay" in setB:
    print("Element availale")
else:
    print('Element not available')

# update
setC = {"pune" , "mumbai" ,"banglore" , "jaipur", "goa"}
print(setC)

setC.update({"wardha","chandrapur"})
print(setC)

setC.update(["nagpur","jabalpur"])
print(setC)

# remove

#remove()
setC2 = {'jabalpur', 'chandrapur', 'jaipur', 'nagpur', 'pune', 'banglore', 'mumbai', 'goa', 'wardha'}
setC2.remove('jaipur')
print(setC2)
print("hello")

# discard()
setC2.discard("pune")
print(setC2)
print('hello')

# pop()
print(setC2)
setC2.pop()
print(setC2)

#clear()
setC2.clear()
print(setC2)

# del
# del setC2
# print(setC2)

# union()
setA = {11,22,33}
setB = {33,44,55,66}
setC3 = setA.union(setB)
print(setC3)


# intersection()
setD = {11,22,33}
setE  = {33,44,55,66}
# setE = setD.intersection(setE)
# print(setE)


# issubset() issuperset()
setG = {11,22,33}
setH = {11,22}
print(setH.issubset(setG))
print(setG.issuperset(setH))

