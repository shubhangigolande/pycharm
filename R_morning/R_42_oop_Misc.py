# MRO
class Employee():
    def show(self):
        print("I am working")


class Pune():
    def show(self):
        print("I am working in Pune")


class Nagpur():
    def show(self):
        print("I am working in Nagpur")


e1 = Employee()
e1.show()     #I am working

p1 = Pune()
p1.show()       #I am working in Pune

n1 = Nagpur()
n1.show()         #I am working in Nagpur





class Employee():
    def show(self):
        print("I am working")


class Pune(Employee):
    def show(self):
        print("I am working in Pune")


class Nagpur(Employee):
    def show(self):
        print("I am working in Nagpur")


e1 = Employee()
e1.show()    #I am working

p1 = Pune()
p1.show()  # it will over ride the parent method    #I am  working in Pune

n1 = Nagpur()
n1.show()  ##it will over ride the parent method      #I am working in Nagpur






class Employee():
    def show(self):
        print("I am working")


class Pune(Employee):
    def show(self):
        print("I am working in Pune")


class Nagpur(Employee):
    def show(self):
        print("I am working in Nagpur")


class D(Pune, Nagpur):
    pass


e1 = Employee()
e1.show()       #I am working

p1 = Pune()
p1.show()  # it will over ride the parent method    #I am working in Pune

n1 = Nagpur()
n1.show()  ##it will over ride the parent method     #I am working in Nagpur

d1 = D()
d1.show()       #I am working in Pune






# method Oreder Resolution MRO
# pref for the method to be used will be from left to right

class Employee():
    def show(self):
        print("I am working")


class Pune(Employee):
    def show(self):
        print("I am working in Pune")


class Nagpur(Employee):
    def show(self):
        print("I am working in Nagpur")


class D(Nagpur, Pune):
    pass


e1 = Employee()
e1.show()      #I am working

p1 = Pune()
p1.show()  # it will over ride the parent method      #I am working in Pune

n1 = Nagpur()
n1.show()  ##it will over ride the parent method      #I am working in Nagpur

d1 = D()
d1.show()         #I am working in Nagpur






# Method over riding
class Animal():
    def make_sound(self):
        print("Some animal Sound")


class Dog(Animal):
    def make_sound(self):
        print("Bark")


class Cat(Animal):
    def make_sound(self):
        print("Meow")


c1 = Cat()
c1.make_sound()  # over riding the parent class

d1 = Dog()
d1.make_sound()  # over riding the parent class
Meow
Bark


# Method Overloading
def add(a, b=0, c=0, d=0):
    print(a + b + c + d)


add(1, 2, 3, 4)        #10
add(1, 2, 3)            #6
add(1, 2)               #3
add(1)                  #1






class Printdata():
    def show(self, *args):
        print(args)


p1 = Printdata()
p1.show(10, 12, 13, 14)      #(10, 12, 13, 14)
p1.show("a", "b", 'c')      #('a', 'b', 'c')




# decorators
class Calc():

    @staticmethod
    def add(x, y):
        print(x + y)

    @staticmethod
    def show():
        print("Welcome to Minskole")


c1 = Calc()
c1.add(12, 12)      #24

c1.show()    # Welcome  to  Minskole


