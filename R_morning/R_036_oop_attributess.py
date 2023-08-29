def sum1(a, b, c):
    print(a + b + c)
sum1(10, 20, 30)    # 60



def mul1(a, b, c):
    print(a * b * c)
mul1(10, 20, 30)    # 6000




class Student():
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def __str__(self):
        return f"The Name of student is {self.name} and roll no is {self.roll} "


s1 = Student("Amit", 100)
print(s1)        # The Name of student is Amit and roll no is 100

s2 = Student("Akash", 101)
print(s2)       # The Name of student is Akash and roll no is 101


s3 = Student("Akhil", 101)
print(s3)         # The Name of student is Akhil and roll no is 101




class Student():
    counter = 0

    def __init__(self, name):
        self.name = name
        Student.counter = Student.counter + 1
        self.roll = Student.counter

    def __str__(self):
        return f"The Name of student is {self.name} and roll no is {self.roll} "


s1 = Student("Amit")
print(s1)       #  The Name of student is Amit and roll no is 1


s2 = Student("Akhil")
print(s2)       # The Name of student is Akhil and roll no is 8

print(s2.counter)        # 8


s3  = Student("Akhil")
print(s3)        # The Name of student is Akhil and roll no is 6

s3.counter = 500
print(s3.counter)       # 500


s5  = Student("Akhil")
print(s5)      #  The Name of student is Akhil and roll no is 7