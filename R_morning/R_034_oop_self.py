# revision
# line by line
# functional programming
# OOP

x = 100
print(type(x))     #  <class 'int'>


class Student():
    def __init__(self):
        self.name = 'Rahul'

s1 = Student()
print(s1)      # < __main__.Student object at 0x0000026EAA02F1F0 >

# print(s1.name)    # Rahul

s2 = Student()
print(s2.name)      # Rahul


class Student():
    def __init__(self, name):
        self.name = name

s1 = Student('Rakesh')
print(s1.name)     # Rakesh

s2 = Student('sameer')
print(s2.name)    # sameer



class Student():
    def __init__(naveen):  # this is called special method , dunder methods ,
        print(id(naveen))    # 2674322427136

s5 = Student()
print(id(s5))        # 2674322427136




class Student():
    def __init__(shaktiman):
        print(id(shaktiman))   # 2674320302400

gangadhar = Student()
print(id(gangadhar))      # 2674320302400




class Student():
    def __init__(self, name, age, area):
        self.name = name
        self.age = age
        self.area = area


s7 = Student('Akash', 24, "Pune")
print(s7.name)   #Akash
print(s7.age)     # 24
print(s7.area)    # Pune


s8 = Student('Sameer', 34, "nasik")
print(s8.name)   # Sameer
print(s8.age)     # 34
print(s8.area)     #nashik



class Student():
    def __init__(self, name, age, area):
        self.n = name
        self.a = age
        self.ar = area

    def __str__(self):
        return f"My name is {self.n} and is from {self.ar} and is {self.a} tears old"


s7 = Student('Akash', 24, "Pune")
print(s7.n)    # Akash
print(s7.a)     # 24
print(s7.ar)     # Pune



x = 100
print(x)    # 100

print(s7)     # < __main__.Student object at 0x0000026EAA43A770 >

print(s7)     # My name is Akash and is from Pune and is 24 tears old