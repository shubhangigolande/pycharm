# creat a class Account
# acc id and balance
# acc 1 , id =1 , bal =100
# acc 2 ; id =2 , bal = 0

class Account():
    counter = 0  # class attribute

    def __init__(self, opening_bal=0):
        Account.counter = Account.counter + 1
        self.id = Account.counter
        self.bal = opening_bal

    def __str__(self):
        return f"Acc  no is : {self.id} and bal is {self.bal}"


a1 = Account(100)
print(a1)       #Acc no is: 1 and bal is 100

a2 = Account()
print(a2)          # Acc no is: 2 and bal is 0






# adding more functionalities to the acc
# deposit
class Account():
    counter = 0  # class attribute

    def __init__(self, opening_bal=0):
        Account.counter = Account.counter + 1
        self.id = Account.counter
        self.bal = opening_bal

    def __str__(self):
        return f"Acc  no is : {self.id} and bal is {self.bal}"

    def deposit(self, amount):
        self.bal = self.bal + amount


a1 = Account(100)
print(a1)      #Acc no is: 1 and bal is 100

a2 = Account()
print(a2)        # Acc no is: 2 and bal is 0

a1.deposit(100)
print(a1)         # Acc no is: 1 and bal is 200







# adding more functionalities to the acc
# withdrawal

class Account():
    counter = 0  # class attribute

    def __init__(self, opening_bal=0):
        Account.counter = Account.counter + 1
        self.id = Account.counter
        self.bal = opening_bal

    def __str__(self):
        return f"Acc  no is : {self.id} and bal is {self.bal}"

    def deposit(self, amount):
        self.bal = self.bal + amount

    def withdraw(self, amount):
        self.bal = self.bal - amount


a1 = Account(100)
print(a1)       #Acc  no is : 1 and bal is 100

a2 = Account()
print(a2)          #Acc  no is : 2 and bal is 0

a1.deposit(100)
print(a1)           #Acc  no is : 1 and bal is 200

a1.withdraw(50)
print(a1)               #Acc  no is : 1 and bal is 150

a1.withdraw(500)
print(a1)               #Acc  no is : 1 and bal is -350







# adding more functionalities to the acc
# withdrawal
#  addding checks on the function


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


a1 = Account(100)
print(a1)               #Acc  no is : 1 and bal is 100

a2 = Account()
print(a2)               #Acc  no is : 2 and bal is 0

a1.deposit(100)
print(a1)               #Acc  no is : 1 and bal is 200

a1.withdraw(50)
print(a1)                   #Acc  no is : 1 and bal is 150


a1.withdraw(500)
print(a1)               #Acc  no is : 1 and bal is 150

a1.deposit(-1000) #no neg amount can be deposited
print(a1)                # Acc  no is : 1 and bal is 150
