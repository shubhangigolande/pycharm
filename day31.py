
print(8+8)
print("hello"+" world")

print(len("chinmay"))
print(len(["sarika","poorva","shraddha","raj"]))
print(len({"firstName":'chinmay',"lastName":'deshpande'}))

class Cat:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def info(self):
        print(self.age + self.name)

    def makeSound(self):
        print("Meow")

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(self.age + self.name)

    def makeSound(self):
        print("Bow Bow")


cat1 = Cat("kiity",2)
dog1 = Dog("moti",2)


q1 = [cat1,dog1]
q2 = [cat1,dog1]
q3 = {
    "obj1":cat1,
    "obj2":dog1
}

for item in q1:
    item.makeSound()


# program 4
# overriding

#overloading - same class ,  same method and differnt signature
#overriding -  different class , same method , same signature



class WorldB():
    def __init__(self, city):
        self.city = city

    def loan(self):
        print("loan implemented from world")
    def save(self):
        print("save implement from world bank")

class SBI(WorldB):
    def loan(self):
        print("I am loan from SBI bank")
    def save(self):
        print("I am save from SBI bank")
    def save(self,p):
        print("I am save from SBI bank")
        print(p)

class PNB(WorldB):
    pass
    # def loan(self):
    #     print("I am loan from PNB bank")
    # def save(self):
    #     print("I am save from PNB bank")

pune  = SBI("pune")
print(pune.city)
pune.save(1)
pune.loan()


goa = PNB("goa")
goa.loan()
goa.save()

class GrandFather():
    def __init__(self,fn,ln):
        self.firstName = fn
        self.lastName  = ln

    def displayName(self):
        print(self.firstName+self.lastName)
class Father(GrandFather):
    def __init__(self, fn, ln, ffn):
       super().__init__(fn,ln)
       self.fname = ffn

    def displayName(self):
        print(self.fname + self.lastName)
        super().displayName()

class Son(Father):

    def __init__(self, fn, ln, ffn,ssn):
       super().__init__(fn,ln,ffn)
       self.sname = ssn
    def displayName(self):
        print(self.sname + self.lastName)
        super().displayName()


chinmay  = Son("manohar","deshpande","shirish","chinmay")
chinmay.displayName()