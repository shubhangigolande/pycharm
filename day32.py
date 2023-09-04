class Person:
    # class level variable
    country = "india"
    def __init__(self,fn,ln,age):
        self.firstName = fn
        self.lastName = ln
        self.age = age

    def displayName(self):
        print(self.firstName + self.lastName)

    def displayCountry(self):
        print(self.country)

    @classmethod
    def changeCourty(cls,newC):
        cls.country = newC

Person.changeCourty("UK")
sarika  =  Person("sarika","pansare",23)
sarika.displayCountry()

poorva  =  Person("poorva","vyas",44)
poorva.displayCountry()

mayuri = Person("Mayuri","Rao",34)
mayuri.displayCountry()

poorva.country = "USA seattle"
poorva.displayCountry()


# program 2
class PersonB:
    def __init__(self,firstName,lasName):
        self.firstName = firstName
        self.lastName = lasName

    # getter()
    def getFirst(self):
        return self.firstName

    # setter()
    def setFirstName(self,fn):
        self.firstName = fn
        return self.firstName

    # setter
    # setcountry
    def setCountry(self,cntry):
        self.country = cntry
        return self.country

amol  = PersonB("amol","rao")
mayuri = PersonB("mayuri","katwe")
mayuri.setFirstName("mayuri p")
mayuri.setCountry("india")

print(mayuri.firstName)
print(mayuri.lastName)
print(mayuri.country)