# inheritance
# program 1
# class Student:
#     firstName = "chinmay"
#     lastName = "deshpande"
#     adharNo = 123
#     def display(self):
#         print(self.firstName + self.lastName)
# class Teacher:
#     firstName = "chinmay"
#     lastName = "deshpande"
#     adharNo = 123
#     salary = 1000
#
#     def display(self):
#         print(self.firstName + self.lastName)
#
#     def displaySalary(self):
#         print(self.salary)
#
# amol = Teacher()
# print(amol.firstName)
# print(amol.lastName)
# print(amol.salary)
# print(amol.adharNo)
#
# amol.displaySalary()
# amol.display()
# program 2
#
# class Student:
#     firstName = "chinmay"
#     lastName = "deshpande"
#     adharNo = 123
#
#     def display(self):
#         print(self.firstName+self.lastName)
#
# class Teacher(Student):
#     salary = 1000
#
#     def displaySalary(self):
#         print(self.salary)
#
# amol = Teacher()
#
# print(amol.firstName)
# print(amol.lastName)
# print(amol.salary)
# print(amol.adharNo)
#
# amol.display()
# amol.displaySalary()

# parent constructor and no constructor in child

# class Student:
#
#     def __init__(self,fn,ln,adharNo):
#         self.firstName = fn
#         self.lastName = ln
#         self.adharNo = adharNo
#
#     def displayName(self):
#         print(self.firstName + self.lastName)
#
#
# class Teacher(Student):
#     salary = 10000
#     def displaySalary(self):
#         print(self.salary)
#
#
# amol = Teacher("amol","rao",12)
# print(amol.firstName)
# print(amol.lastName)
# print(amol.salary)
# print(amol.adharNo)
#
# amol.displaySalary()
# amol.displayName()

# program 4
# constructor in parent as well as in child


class Student:

    def __init__(self,fn,ln,adharNo):
        self.firstName = fn
        self.lastName = ln
        self.adharNo = adharNo

    def displayName(self):
        print(self.firstName+ self.lastName)

class Teacher(Student):

    def __init__(self,fn,ln,adharNo,sl):
        super().__init__(fn,ln,adharNo)
        self.salary = sl

    def displaySalary(self):
        print(self.salary)

amol = Teacher("amol","rao",23,1000)
print(amol.firstName)
print(amol.lastName)
print(amol.salary)
print(amol.adharNo)
amol.displaySalary()
amol.displayName()