# creating two classes for SA and CA

class Account():
    counter = 0  # class attribute

    def __init__(self, opening_bal=0):
        Account.counter = Account.counter + 1
        self.id = Account.counter
        self.bal = opening_bal

    def __str__(self):
        return f"Acc  no is : {self.id} and bal is {self.bal}"

    def deposit(self, amount):
        if amount > 0:
            self.bal = self.bal + amount

    def withdraw(self, amount):
        if amount > 0 and self.bal >= amount:
            self.bal = self.bal - amount


class SavingsAccount():
    pass


class CurrentAcocut():
    pass


sa1 = SavingsAccount()
ca1 = CurrentAcocut()
print(sa1)    #< __main__.SavingsAccount object at 0x00000229490992D0 >
print(ca1)    #< __main__.CurrentAcocut object at 0x0000022949099240 >




# inheriting the Account class to CA class and SA class
class Account():
    counter = 0  # class attribute

    def __init__(self, opening_bal=0):
        Account.counter = Account.counter + 1
        self.id = Account.counter
        self.bal = opening_bal

    def __str__(self):
        return f"Acc  no is : {self.id} and bal is {self.bal}"

    def deposit(self, amount):
        if amount > 0:
            self.bal = self.bal + amount

    def withdraw(self, amount):
        if amount > 0 and self.bal >= amount:
            self.bal = self.bal - amount


class SavingsAccount(Account):
    pass


class CurrentAcocut(Account):
    pass


sa1 = SavingsAccount()
ca1 = CurrentAcocut()
print(sa1)      # Acc no is: 1 and bal is 0
print(ca1)      #Acc no is: 2 and bal is 0

sa1.deposit(100)
ca1.deposit(100)

print(sa1)     #Acc no is: 1 and bal is 100
print(ca1)      #Acc no is: 2 and bal is 100


# adding restriction on the no of tx
# SA to have max 5 tx limit
# CA to have max 100 tx

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


class CurrentAcocut(Account):
    pass


sa1 = SavingsAccount()
ca1 = CurrentAcocut()
print(sa1)     #Acc no is: 1 and bal is 0
print(ca1)     # Acc no is: 2 and bal is 0

sa1.deposit(100)
ca1.deposit(100)

sa1.deposit(100)
sa1.deposit(100)
sa1.deposit(100)
sa1.deposit(100)
sa1.deposit(100)

sa1.deposit(100)  # this tx as failed
sa1.withdraw(100)  # failed tx
print(sa1)     # Acc no is: 1 and bal is 500
print(ca1)    # Acc no is: 2 and bal is 100






# adding restriction on the no of tx
# SA to have max 5 tx limit
# increaing the default 5 tx to 100 for thhe CA class
# CA to have max 100 tx

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
        self.max_tx = 100


sa1 = SavingsAccount()
ca1 = CurrentAcocut()
print(sa1)         #Acc no is: 1 and bal is 0
print(ca1)

sa1.deposit(100)
ca1.deposit(100)

sa1.deposit(100)
sa1.deposit(100)
sa1.deposit(100)
sa1.deposit(100)
sa1.deposit(100)

sa1.deposit(100)  # this tx as failed
sa1.withdraw(100)  # failed tx
print(sa1)
print(ca1)

# O/P ---------------------------------------------------------------------------
# AttributeError        Traceback(most recent call last)
# Input In[15], in < cell line: 36 > ()
# 34 ca1 = CurrentAcocut()
# 35 print(sa1)
# ---> 36 print(ca1)
# 38 sa1.deposit(100)
# 39 ca1.deposit(100)
#
# Input In[15], in Account.__str__(self)
# 14 def __str__(self):
#
# ---> 15      return f"Acc  no is : {self.id} and bal is {self.bal}"
#
# AttributeError: 'CurrentAcocut' object has no attribute 'id'






# adding restriction on the no of tx
# SA to have max 5 tx limit
# increaing the default 5 tx to 100 for thhe CA class
# CA to have max 100 tx
# using super method to call the parent __init__()
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
print(sa1)      # Acc no is: 1 and bal is 0
print(ca1)      #Acc no is: 2 and bal is 0

sa1.deposit(100)
ca1.deposit(100)

sa1.deposit(100)
sa1.deposit(100)
sa1.deposit(100)
sa1.deposit(100)
sa1.deposit(100)

sa1.deposit(100)  # this tx as failed
sa1.withdraw(100)  # failed tx

ca1.deposit(100)
ca1.deposit(100)
ca1.deposit(100)
ca1.deposit(100)
ca1.deposit(100)

ca1.deposit(900)
ca1.deposit(900)

ca1.deposit(900)

ca1.deposit(900)

ca1.deposit(900)

sa1.deposit(1000)

print(sa1)     #Acc no is: 1 and bal is 500
print(ca1)      #Acc no is: 2 and bal is 5100





