#HOw to write/organise the code

# line by line

print("Hello World")    #Hello World
print("We will make addition of two numbers")    #We will make addition of two numbers
print(10+20)     # 30



# functional programming
def greet():
    print("Hello World")    #Hello World

def calc():
    print("We will make addition of two numbers")    # We will make addition of two numbers
    print(10+20)    #30

greet()
calc()

greet()     #Hello World




# OOP
# Object oriented Programming

# School>>
# students
# teachers
# subjects
# exams



# bank >>>
# customers
# accounts
# transactions
# debit/credit


# how to create a class
class Student():
    pass
print(Student())    #<__main__.Student object at 0x000001BD70B9AE00>

s1 = Student()
print(s1)     # <__main__.Student object at 0x000001BD70B9A980>

s2 = Student()
print(s2)      # <__main__.Student object at 0x000001BD71085A20>

s1.name = "Rahul"
print(s1.name)     # Rahul

s2.name = "Mahesh"
print(s2.name)     #Mahesh

s1.place = "Nasik"
print(s1.place)     # Nasik

s2.place = "Nagpur"
print(s2.place)     #Nagpur