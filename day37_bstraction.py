# abstraction hiding unnecesarry details
# abstract class dont have an object,bt the child class have an object.
# abstract class use for @abstractmethod
# child classes inherites father class method but not allow internal data in method ,
# in that case child class create own data for abstract method.
# in python provide abstract 'abc' module.

from  abc import ABC ,abstractmethod

class worldBank(ABC):
    @abstractmethod
    def loan(self):
        pass
    @abstractmethod
    def save(self):
        pass

class SBI(worldBank):
    def loan(self):
        print('i m loan form SBI')

    def save(self):
        print('i m save from SBI')

class PNB(worldBank):
    def loan(self):
        print('i m loan from PNB')
    def save(self):
        print('i m save from PNB')
    def pnbinterest(self):
        print('i m pnbinterest from PNB')



pune = SBI()
pune.loan()
pune.save()


bmt=PNB()
bmt.loan()
bmt.save()
bmt.pnbinterest()


# 2 program

class Animal(ABC):
    @abstractmethod
    def move(self):
        pass
    def categary(self):
        print('Animals')

class Human(Animal):
    def move(self):
        print('I can Walk')

class snake(Animal):
    def move(self):
        print('I can Crawl')

class dog(Animal):
    def move(self):
        print('I  Can Bark')

class tiger(Animal):
    def move(self):
        print('I can Roar')

h1=Human()
h1.move()
h1.categary()



snake1=snake()
snake1.move()
snake1.categary()



dog1=dog()
dog1.move()
dog1.categary()


tiger1=tiger()
tiger1.move()
tiger1.categary()




#main class have dont object
# #us = WorldBank()
# #Can't instantiate abstract class WorldBank with abstract methods loan, save
