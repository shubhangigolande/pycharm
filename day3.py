
# numT > 0 && numT <= 5   =======> 10 % discount
# numT > 5 && numT <= 10  =======> 20 % discount
# num > 10                =======> 30 % dicount

numT = 11
if(numT >0 and numT <= 5):
    print("10 % discount")
if(numT > 5 and numT <= 10):
    print("20 % discount")
if(numT > 10):
    print("30 % discount")

# program 2

numTa = -34

if(numTa > 0 and numTa <= 5):
    print('10 % discount')
elif(numTa > 5 and numTa <= 10):
    print('20 % discount')
elif(numTa > 10):
    print("30 % discount")
else:
    print("Incorrect value")

marks = 92
if(marks > 90):
    print('Grade A')
if(marks > 75):
    print('Grade B')
if(marks >65):
    print('Grade C')

marks = 67
if(marks > 90):
    print('Grade A')
elif(marks > 75):
    print('Grade B')
elif(marks >65):
    print('Grade C')
else:
    print('Fail .. please try again')


# program 3

q1 = 10
q2 = 5

if(q1 > q2):
    print('q1 is greater')
else:
    print('q2 is greater')

x1 = 10
x2 = 50
x3 = 300

if(x1 > x2 and x1 > x3):
    print("x1 is greater")
elif(x2 > x1 and x2 > x3):
    print("x2 is greater")
else:
    print("x3 is greater")


q11 = 10
q12 = 50
print("q11 is greater") if q11 > q12 else print("q12 is greater")


"""
age = 17
q = "can driver" if age >= 18 else "cannot drive"
print(q)
"""


