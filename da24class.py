# class Person:
#     age = 34
#     fullName= "chinmay deshpande"
#     rollNo = 30
#
#     def talk(self):
#         print("i am talking ")
#     def walk(self):
#         print("I am walking")
#
#
# amol = Person()
# print(amol.age)
# print(amol.fullName)
# print(amol.rollNo)
# amol.talk()
# amol.walk()
#
#
# chinmay = Person()
# print(chinmay.age)
# print(chinmay.fullName)
# print(chinmay.rollNo)
# chinmay.talk()
# chinmay.walk()
#
# chinmay.age = 77
# chinmay.fullName = "chinmay s deshpande"
# chinmay.rollNo = 67
#
# print(chinmay.age)
# print(chinmay.fullName)
# print(chinmay.rollNo)

# program 2

class Person2:
    def __init__(self,fn,ag,rn):
        self.fullName = fn
        self.age = ag
        self.rollNo = rn

    def display(self):
        print(self.fullName)

amol2 = Person2('amol rao',23,45)
chinmay2  = Person2('chinmay deshpande',44,55)

amol2.display()
chinmay2.display()