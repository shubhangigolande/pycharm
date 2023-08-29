# program 1
class Person:
    #hardcoded values
    age = 10
    fullName = "chinmay deshpande"
    skills = ["python","java","javascript","html",'css']
    def noOfSkills(self):
        print(len(self.skills))
    def displayFullName(self):
        print(self.fullName)

amol  = Person()
print(amol.age)
print(amol.fullName)
print(amol.skills)
amol.displayFullName()
amol.noOfSkills()

chinmay = Person()
print(chinmay.age)
print(chinmay.fullName)
print(chinmay.skills)
chinmay.displayFullName()
chinmay.noOfSkills()

chinmay.age = 12
chinmay.fullName = "chinmay s deshpande"
chinmay.skills = ["salesforce","html"]

chinmay.displayFullName()
chinmay.noOfSkills()

# program 2

class Person2:
    def __init__(self,fn,age,rn,skills):
        self.fullName = fn
        self.age = age
        self.rollNo = rn
        self.skills = skills

    def noOfSkills(self):
        print(len(self.skills))
    def displayFullName(self):
        print(self.fullName)

amit = Person2("amit kumar",23,4,["javascript","python","cypress"])
print(amit.skills)
print(amit.age)
print(amit.rollNo)
print(amit.fullName)
amit.noOfSkills()
amit.displayFullName()


students  = [
    Person2("amit kumar",25,40,["javascript","python","cypress"]),
    Person2("poorva kumar",25,40,["javascript","python","cypress"]),
    Person2("sarika kumar",25,40,["javascript","python","sql"]),
    Person2("ram kumar",25,40,["javascript","python","cypress"]),
    Person2("satish kumar",25,40,["javascript","python","cypress"])
]


studentss = {
    "student1": Person2("amit kumar",25,40,["javascript","python","cypress"]),
    "student2": Person2("amit kumar",25,40,["javascript","python","cypress"]),
    "student3": Person2("amit kumar",25,40,["javascript","python","cypress"]),
    "student4": Person2("amit kumar",25,40,["javascript","python","cypress"]),
    "student5": Person2("amit kumar",25,40,["javascript","python","cypress"])

}

for k,v in studentss.items():
    print(k,v)
    v.noOfSkills()
    v.displayFullName()

for k in studentss.keys():
    studentss.get(k).noOfSkills()
    studentss.get(k).displayFullName()

for v in studentss.values():
    v.noOfSkills()
    v.displayFullName()

for k in studentss:
    studentss[k].noOfSkills()
    studentss[k].displayFullName()

for item in students:
    item.displayFullName()
    item.noOfSkills()

for item in range(len(students)):
    students[item].displayFullName()
    students[item].noOfSkills()