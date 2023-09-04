
# program 1
# Single inheritance
class Student:
    def __init__(self,fn,ln):
        self.firstName = fn
        self.lastName = ln

    def displayName(self):
        print(self.firstName + self.lastName)

class Teacher(Student):

    def __init__(self,fn,ln,sl):
        super().__init__(fn,ln)
        self.salary = sl

    def displaySalary(self):
        print(self.salary)

amol = Teacher("amol","rao",10000)
print(amol.firstName)
print(amol.lastName)
print(amol.salary)
amol.displayName()
amol.displaySalary()

# Program 2
# Multilevel

class GrandFather:

    def __init__(self,fn,ln):
        self.firstName = fn
        self.lastName = ln

    def displayGName(self):
        print(self.firstName,self.lastName)

class Father(GrandFather):
    def __init__(self,fn,ln,fnn):
        super().__init__(fn,ln)
        self.fname = fnn

    def displayFName(self):
        print(self.fname + self.lastName)

class Son(Father):
    def __init__(self,fn,ln,fnn,snn):
        super().__init__(fn,ln,fnn)
        self.sname = snn

    def displaySName(self):
        print(self.sname + self.lastName)

chinmay = Son("monhoar","deshpande","shirsh","chinmay")

chinmay.displaySName()
chinmay.displayFName()
chinmay.displayGName()


# program
# Heriachial inhertance


class Father:

    def __init__(self,fn,ln):
        self.firstName  = fn
        self.lastName = ln

    def displayFN(self):
        print(self.firstName + self.lastName)

class Son(Father):
    def __init__(self,fn,ln,sn):
        super().__init__(fn,ln)
        self.sname = sn

    def displaySN(self):
        print(self.sname + self.lastName)


class Daughter(Father):
    def __init__(self, fn, ln, dn):
        super().__init__(fn, ln)
        self.dname = dn

    def displayDN(self):
        print(self.dname + self.lastName)


amol = Son("diplip","rao","amol")
mayuri = Daughter("dilip","rao","mayuri")

amol.displayFN()
amol.displaySN()

mayuri.displayFN()
mayuri.displayDN()




# program 4 -
# Multiple interitance

class FatherA():
    def __init__(self,fn,ln):
        self.firstName = fn
        self.lastName =ln

    def displayPName(self):
        print("I am from father class")
        print(self.firstName + self.lastName)

class MotherA():
    def __init__(self, fn, ln):
        self.firstName = fn
        self.lastName = ln

    def displayPName(self):
        print("I am from mother class")
        print(self.firstName + self.lastName)

class SonA(FatherA,MotherA):
    def __init__(self,pn, ln ,sn):
        super().__init__(pn,ln)
        self.sname = sn

    def displaySn(self):
        print(self.sname+ self.lastName)

chinmay = SonA("kanchan","deshpande","chinmay")
chinmay.displayPName()

#Method order resolution