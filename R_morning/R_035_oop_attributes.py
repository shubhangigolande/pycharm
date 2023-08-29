x = 100
print(type(x))      # <class 'int'>


class Student:
    def __init__(self, name, age, area):
        self.name = name
        self.age = age
        self.area = area


s7 = Student('Akash', 24, "Pune")
print(s7.name)      #Akash
print(s7.age)      # 24
print(s7.area)     #Pune



class Student():
    def __init__(self):
        print("Hello World")

s7 = Student()     # Hello World




class Student():
    def greet(self):
        print("Hello World")     #Hello World


s7 = Student()
print(s7.greet())     #None





class Student():
    def __init__():
        print("Hello World")


s7 = Student()
# O/P :=>---------------------------------------------------------------------------
# TypeError       Traceback(most recent call last)
# Input In[12], in < cell line: 5 > ()
# 2  def __init__():
#     3  print("Hello World")
# ----> 5  s7 = Student()
#
# TypeError: Student.__init__() takes 0 positional arguments but 1 was given




class Student():

    def __init__(self):
        print("Hello World")
s7 = Student()    # Hello World



class Student():
    def __init__(self, name):
        self.name = name

    def __init__(self, age):
        self.age = age


# s7 = Student("Rakesh")
s7 = Student(25)
# s7.name
s7.age         # 25