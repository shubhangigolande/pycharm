


class Student:
    def __init__(self,firstName, lastName , adharNo):
        self.firstName = firstName
        self.lastName = lastName
        self.adharNo = adharNo

    def displayName(self):
        print(self.firstName+self.lastName)


class Teacher(Student):
    def __init__(self,firstName, lastName , adharNo,salary):
        super().__init__(firstName, lastName , adharNo)
        self.salary = salary

    def displaySalary(self):
        print(self.salary)

amol = Teacher("amol","rao",123,5000)
print(amol.firstName)
print(amol.lastName)
print(amol.adharNo)
print(amol.salary)
amol.displaySalary()
amol.displayName()

class GrandFather:

    def __init__(self,firstName , lastName):
        self.firstName = firstName
        self.lastName = lastName

    def displayGN(self):
        print(self.firstName + self.lastName)


class Father(GrandFather):
    def __init__(self,firstName , lastName, ffirstName):
            super().__init__(firstName , lastName)
            self.ffirstName = ffirstName

    def displayFN(self):
        print(self.ffirstName + self.lastName)


class Son(Father):
    def __init__(self, firstName, lastName, ffirstName, sname):
        super().__init__( firstName, lastName, ffirstName)
        self.sname = sname

    def displaySN(self):
        print(self.sname + self.lastName)

chinmay = Son("manohar","deshpande","shirish","chinmay")
print(chinmay.firstName)
print(chinmay.lastName)
print(chinmay.ffirstName)
print(chinmay.sname)
chinmay.displayGN()
chinmay.displayFN()
chinmay.displaySN()


class Mother:
    def __init__(self,mname,mlastName):
        self.firstName = mname
        self.lastName = mlastName

    def displayMName(self):
        print(self.firstName + self.lastName)

class Son(Mother):
    def __init__(self ,mname,mlastName, sname):
        super().__init__(mname,mlastName)
        self.sname = sname

    def displaySName(self):
        print(self.sname + self.lastName)


class Daughter(Mother):
    def __init__(self, mname, mlastName, dname):
        super().__init__(mname, mlastName)
        self.dname = dname

    def displayDName(self):
        print(self.dname + self.lastName)

#kanchan = Mother("kanchan","deshpande")

chinmay = Son("kanchan","deshpande","chinmay")
gauri = Daughter("kanchan","deshpande","gauri")


print(chinmay.sname)
print(chinmay.firstName)
print(chinmay.lastName)
chinmay.displayMName()
chinmay.displaySName()

print(gauri.dname)
print(gauri.firstName)
print(gauri.lastName)
gauri.displayMName()
gauri.displayDName()