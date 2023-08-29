# program 1
#append()
vegi = ['brinjal','potato','tomato','cabbage']
vegi.append('cauliflower')
print(vegi)


# program 2
# clear()
vegi.clear()
print(vegi)


# program3

vegi = ['brinjal','potato','tomato','cabbage']
veg=vegi
veg[0]='brocoli'
print(vegi)
print(veg)


# program 4
nums=[44,55,66]
numb=nums.copy()
numb[1]=85
print(numb)
print(nums)



# program 5
numberss=[11,22,33,44,55,66,77,88,99]
ww=numberss.count(54)
print(ww)

numberH = [22,33,44,55,22,33,44,55]
q1 = numberH.count(22)
print(q1)

# program 6
gnm=['swara','mahi','aarya']
bnm=['shiv','ansh','dev']
bnm.extend(gnm)
print(bnm)

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