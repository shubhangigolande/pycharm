class India():
    def capital(self):
        print("New Delhi")


class Nepal():
    def capital(self):
        print("Kathamandu")


class SriLanka():
    def capital(self):
        print("Jaywardhanepuram")


ind = India()
nep = Nepal()
sl = SriLanka()

ind.capital()       #New Delhi
nep.capital()      #Kathamandu
sl.capital()     #Jaywardhanepuram





a = 100
b = "Ramesh"

print(a)    # 100
print(b)     # Ramesh





# THIS IS SYMBOLIC IN NATURE
# SA INterest = 3%
# CA interes = 0%


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
    def __init__(self):
        super().__init__()

    def get_interest(self):
        return self._Account__bal * 0.03  # calling the valua after name mangling


class CurrentAcocut(Account):  # __init__ > id, bal,max_tx,num_tx
    def __init__(self):
        super().__init__()
        self.max_tx = 100

    def get_interest(self):
        return 0


sa1 = SavingsAccount()
ca1 = CurrentAcocut()
print(sa1)     # Acc no is: 1 and bal is 0
print(ca1)     #Acc no is: 1 and bal is 0

sa1.deposit(100)
ca1.deposit(100)

print(sa1)       # Acc no is: 1 and bal is 100
print(ca1)      #  Acc no is: 2 and bal is 100

sa1._bal = 500
print(sa1)     # Acc no is: 1 and bal is 100

sa1.deposit(1000)
ca1.deposit(100)

print(sa1)       # Acc no is: 1 and bal is 1100
print(ca1)        #Acc no is: 2 and bal is 200

print(sa1.get_interest())        # 33.0
print(ca1.get_interest())     # 0




# THIS IS SYMBOLIC IN NATURE
# SA INterest = 3%
# CA interes = 0%


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
    def __init__(self):
        super().__init__()

    def get_sa_interest(self):
        return self._Account__bal * 0.03  # calling the valua after name mangling


class CurrentAcocut(Account):  # __init__ > id, bal,max_tx,num_tx
    def __init__(self):
        super().__init__()
        self.max_tx = 100

    def get_ca_interest(self):
        return 0


sa1 = SavingsAccount()
ca1 = CurrentAcocut()
print(sa1)     #Acc no is: 1 and bal is 0
print(ca1)     #Acc no is: 2 and bal is 0

sa1.deposit(100)
ca1.deposit(100)

print(sa1)      #Acc no is: 1 and bal is 100
print(ca1)      #Acc no is: 2 and bal is 100

sa1._bal = 500
print(sa1)      #Acc no is: 1 and bal is 100

sa1.deposit(1000)
ca1.deposit(100)

print(sa1)      #Acc no is: 1 and bal is 1100
print(ca1)       #Acc no is: 2 and bal is 200

# this is not polymorphism
print(sa1.get_sa_interest())       #33.0
print(ca1.get_ca_interest())      # 0
