#################################################
#  20.07.2023 9.00AM
#################################################
#  TOPICS TO BE COVERED
# 👉 Control Flow statements, if..else
# 👉 Bool  in Python
#################################################

print(bool())

# if
# Syntex
# if <condition>:
# code/suit/statement


print("You have passed the exam !!! wow !!!")

score = 74
pass_marks = 40

if score >= pass_marks:
    print("You have passed the exam !!! wow !!!")

score = 38
pass_marks = 40

if score >= pass_marks:
    print("You have passed the exam !!! wow !!!")

# if...else
# Syntex
# if <condition>:
# code/suit/statement
# else:
# code/suit/statement


score = 38
pass_marks = 40

if score >= pass_marks:
    print("You have passed the exam !!! wow !!!")
else:
    print("Please try next time !!!")

#  avoid this below case
score = 40
pass_marks = 40

if score > pass_marks:  # we have to consider the boundary condition
    print("You have passed the exam !!! wow !!!")
else:
    print("Please try next time !!!")

print(100 % 25)  # will get the remainder as o/p
print(101 % 25)  # will get the remainder as o/p
print(13 % 2)  # will get the remainder as o/p
print(12 % 2)  # will get the remainder as o/p
print(11 % 2)  # will get the remainder as o/p

# o/p is zero means the num is even else odd

num = 16

if num % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

num2 = 109

if num2 % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

passwd = "abc@1234"
print(passwd)
print(len(passwd))

if len(passwd) >= 8:
    print("Password is strong")
else:
    print("Password is weak")

print(len(passwd) >= 8)  # checking the bool value

# HW

# if:
#     print("Good")
# else:
#     print("Bad")