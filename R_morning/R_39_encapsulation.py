#  PUBLIC VARIABLE


class Account():
    counter = 0  # class attribute

    def __init__(self, opening_bal=0):
        Account.counter = Account.counter + 1
        self.id = Account.counter
        self.bal = opening_bal
        self.num_tx = 0
        self.max_tx = 5

    def __str__(self):
        return f"Acc  no is : {self.id} and bal is {self.bal}"

    def deposit(self, amount):
        if amount > 0 and self.num_tx < self.max_tx:
            self.bal = self.bal + amount
            self.num_tx = self.num_tx + 1

    def withdraw(self, amount):
        if amount > 0 and self.bal >= amount and self.num_tx < self.max_tx:
            self.bal = self.bal - amount
            self.num_tx = self.num_tx + 1


class SavingsAccount(Account):
    pass


class CurrentAcocut(Account):  # __init__ > id, bal,max_tx,num_tx
    def __init__(self):
        super().__init__()
        self.max_tx = 100


sa1 = SavingsAccount()
ca1 = CurrentAcocut()
print(sa1)      #Acc no is: 1 and bal is 0
print(ca1)      #Acc no is: 2 and bal is 0

sa1.deposit(100)
ca1.deposit(100)

print(sa1)      #Acc no is: 1 and bal is 100
print(ca1)      #Acc no is: 2 and bal is 100

sa1.bal = 500000000000000000000
print(sa1)    #Acc no is: 1 and bal is 500000000000000000000





 # PRIVATE VARAIBLE

# hiding attribute using Name Mangling

class Account():
    counter = 0  # class attribute

    def __init__(self, opening_bal=0):
        Account.counter = Account.counter + 1
        self.id = Account.counter
        self.__bal = opening_bal
        self.num_tx = 0
        self.max_tx = 5

    def __str__(self):
        return f"Acc  no is : {self.id} and bal is {self.__bal}"

    def deposit(self, amount):
        if amount > 0 and self.num_tx < self.max_tx:
            self.__bal = self.__bal + amount
            self.num_tx = self.num_tx + 1

    def withdraw(self, amount):
        if amount > 0 and self.__bal >= amount and self.num_tx < self.max_tx:
            self.__bal = self.__bal - amount
            self.num_tx = self.num_tx + 1


class SavingsAccount(Account):
    pass


class CurrentAcocut(Account):  # __init__ > id, bal,max_tx,num_tx
    def __init__(self):
        super().__init__()
        self.max_tx = 100


sa1 = SavingsAccount()
ca1 = CurrentAcocut()
print(sa1)     # Acc no is: 1 and bal is 0
print(ca1)    # Acc no is: 2 and bal is 0

sa1.deposit(100)
ca1.deposit(100)

print(sa1)     #Acc no is: 1 and bal is 100
print(ca1)     #Acc no is: 2 and bal is 100

sa1.__bal = 500000000000000000000
print(sa1)      #Acc no is: 1 and bal is 100

print(sa1.__bal)         #500000000000000000000

# Name Mangling
# Renaming the private variable
# __bal is now used as _Account__bal


print(sa1._Account__bal)         #100

sa1.deposit(100)
print(sa1._Account__bal)           #200

print(sa1.__bal)          #500000000000000000000






# PROTECTED VARIABLE

# THIS IS SYMBOLIC IN NATURE

class Account():
    counter = 0  # class attribute

    def __init__(self, opening_bal=0):
        Account.counter = Account.counter + 1
        self.id = Account.counter
        self._bal = opening_bal
        self.num_tx = 0
        self.max_tx = 5

    def __str__(self):
        return f"Acc  no is : {self.id} and bal is {self._bal}"

    def deposit(self, amount):
        if amount > 0 and self.num_tx < self.max_tx:
            self._bal = self._bal + amount
            self.num_tx = self.num_tx + 1

    def withdraw(self, amount):
        if amount > 0 and self._bal >= amount and self.num_tx < self.max_tx:
            self._bal = self._bal - amount
            self.num_tx = self.num_tx + 1


class SavingsAccount(Account):
    pass


class CurrentAcocut(Account):  # __init__ > id, bal,max_tx,num_tx
    def __init__(self):
        super().__init__()
        self.max_tx = 100


sa1 = SavingsAccount()
ca1 = CurrentAcocut()
print(sa1)     #Acc no is: 1 and bal is 0
print(ca1)    # Acc no is: 2 and bal is 0

sa1.deposit(100)
ca1.deposit(100)

print(sa1)     #Acc no is: 1 and bal is 100
print(ca1)      #  Acc no is: 2 and bal is 100

sa1._bal = 500
print(sa1)        # Acc no is: 1 and bal is 500





