# public variable

class Person:
    # class level variable
    country = "india"

    def __init__(self, fn, ln, age):
        self.firstName = fn
        self.lastName = ln
        self.age = age

    def displayName(self):
        print(self.firstName + self.lastName, "age is :", self.age)

    def displayCountry(self):
        print(self.country)


akash = Person("Akash", "Patil", 23)
akash.displayName()

print(akash.age)
akash.age = 17
print(akash.age)

akash.displayName()
# O/P:-
# AkashPatil age is: 23
# 23
# 17
# AkashPatil age is: 17




# private variable
# this is only symbolic

class Person:
    # class level variable
    country = "india"

    def __init__(self, fn, ln, age):
        self.firstName = fn
        self.lastName = ln
        self._age = age

    def displayName(self):
        print(self.firstName + self.lastName, "age is :", self._age)

    def displayCountry(self):
        print(self.country)


akash = Person("Akash", "Patil", 23)
akash.displayName()

# print(akash.age)
akash.age = 17
print(akash.age)
print(akash._age)
akash.displayName()

akash._age = 13  # such changes will not be approved
akash.displayName()
#O/P:-
# AkashPatil age is: 23
# 17
# 23
# AkashPatil age is: 23
# AkashPatil age is: 13





# Protected variable

class Person:
    # class level variable
    country = "india"

    def __init__(self, fn, ln, age):
        self.firstName = fn
        self.lastName = ln
        self.__age = age

    def displayName(self):
        print(self.firstName + self.lastName, "age is :", self.__age)

    def displayCountry(self):
        print(self.country)


akash = Person("Akash", "Patil", 23)
akash.displayName()

akash.__age = 17
akash.displayName()

print(akash.__age)
akash.displayName()

# Name mangling
# akash.__age is renamed as  akash._Person__age after name mangling

akash.displayName()
akash._Person__age = 99

akash.displayName()
# O/P:-
# AkashPatil age is: 23
# AkashPatil age is: 23
# 17
# AkashPatil age is: 23
# AkashPatil age is: 23
# AkashPatil age is: 99





# Protected variable

class Person:
    # class level variable
    country = "india"

    def __init__(self, fn, ln, age, place):
        self.firstName = fn
        self.lastName = ln
        self.__age = age  # protected
        self.__place = place  # protected

    def displayName(self):
        print(self.firstName + self.lastName, "age is :", self.__age, "is from ", self.__place)

    def displayCountry(self):
        print(self.country)


akash = Person("Akash", "Patil", 23, 'Pune')
akash.displayName()

akash.__age = 17
akash.displayName()

print(akash.__age)
akash.displayName()

# Name mangling
# akash.__age is renamed as  akash._Person__age after name mangling

akash.displayName()
akash._Person__age = 99

akash.displayName()

akash.__place = "Beed"  # a new attribute with name .__place is created
print(akash.__place)

akash.displayName()

print(akash._Person__place)

akash._Person__place = "Nanded"
akash.displayName()
#O/P:-
# AkashPatil age is: 23 is from Pune
# AkashPatil age is: 23 is from Pune
# 17
# AkashPatil age is: 23 is from Pune
# AkashPatil age is: 23 is from Pune
# AkashPatil age is: 99 is from Pune
# Beed
# AkashPatil age is: 99 is from Pune
# Pune
# AkashPatil age is: 99 is from Nanded
