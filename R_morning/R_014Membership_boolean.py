#################################################
#  19.07.2023 9.00AM
#################################################
#  TOPICS TO BE COVERED
# 👉 Membership Operators in Python
# 👉 Bool  in Python
#################################################



#  Membership Operators:
#   - In (in)
#   - Not in (not in)



list_vo = ['A', 'E', 'I', 'O', 'U']

print("a" in list_vo) #case sensitive
print("A" in list_vo) #case sensitive
print("Z" not in list_vo) #case sensitive
print("A" not in list_vo) #case sensitive




# boolean o/p of data types

print(1)
print(bool(1))

print('1')
print(bool('1'))

print(0)
print(bool(0))


print('0')
print(bool('0'))


print("True")
print(bool("True"))
print(bool(True))

print("False")
print(bool("False"))
print(bool(False))



print(10)
print(bool(10))


print(00)
print(bool(00))


print(0.0)
print(bool(0.0))



print([1,2,3,4,5])
print(bool([1,2,3,4,5]))
print(bool([1]))
print(bool([])) #False



print((1,2,3,4,5))
print(type((1,2,3,4,5)))
print(bool((1,2,3,4,5)))
print(bool((1,2)))
print(bool((1,)))
print(type((1,))) #this is a tuple

print(type((1))) #for good readibility
print(bool(())) #the data type is empty
print(bool((""))) #the data type is empty
print(bool(("1"))) #the data type is empty


print((" "))
print(bool(" "))