

setA  = {"chinmay","samay","ram","sham","chinmay"}
print(setA)

# add()
setA.add("komal")
print(setA)

# clear()
# setA.clear()
# print(setA)


# copy()
setC  =  {11,22,33}
#setD  = setC
# setC.remove(11)
# print(setC)
# print(setD)

# setE  = setC.copy()
# setE.remove(11)
# print(setE)
# print(setC)


# difference()
setA = {11,22,33}
setB = {11,22,44}
print(setA.difference(setB))
print(setB.difference(setA))

# differenceUpdate()
setC = {11,22,33}
setD = {11,22,44}

#print(setC.difference(setD))
setC.difference_update(setD)
print(setC)

#discard()
setR = {11,22,33,44}
setR.discard(22)
print(setR)

#interection()

setG = {11,22,33,44}
setH  = {11,22,55,66}
print(setG.intersection(setH))

# intersection_update()
setG.intersection_update(setH)
print(setG)


#isdisjoint()
setQ  = {11,22,33}
setH = {44,55,22}
print(setQ.isdisjoint(setH))

#issuperset() #issubset()

setI = {11,22,33}
setH = {11,22}
print(setI.issuperset(setH))
print(setH.issubset(setI))

# pop()
setI.pop()

# remove()
setI.remove(22)

#union
setQ = {11,22,33,44}
setL = {44,55,66}
setS = setQ.union(setL)
print(setS)

#update()
setQ.update({444,555})
print(setQ)
setQ.update([666,7777,88888])
print(setQ)


#symmetric difference()
k = {1,2,3}
l = {1,4,6}
print(k.symmetric_difference(l))

k.symmetric_difference_update(l)
print(k)