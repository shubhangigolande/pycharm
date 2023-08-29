class Bank:
    def __init__(self,fn,accno,bal):
        self.fullName = fn
        self.account = accno
        self.balance = bal
        self.transactions = []
        # deposit()
    def deposit(self,amount):
            self.balance = self.balance + amount
            self.transactions.append(amount)
            return self.balance
    # withdrawl()
    def withdrawl(self,amount):
        if(self.balance > amount):
            self.balance = self.balance - amount
            self.transactions.append(amount)
        else:
            print("in sufficient balance")

    # last5transactions
    def lastFiveTransactions(self):
        return self.transactions[-5:]


amol = Bank("amol rao",123,1000)
sarika = Bank("sarika pansare",123,500)
chinmay = Bank("chinmay deshpande",123,100000000)
shubhangi = Bank("shubhangi pawar",123,600)
amit = Bank("amit kumar",123,100000)


accs = [amol,sarika,chinmay,shubhangi,amit]
for acc in accs:
    print(acc.balance)
for acc in accs:
    print(acc.fullName)
for acc in accs:
    print(acc.transactions)

# deposit()

for acc in accs:
    acc.deposit(100000)
    acc.deposit(100)
    acc.deposit(10)
    acc.deposit(100)

for acc in accs:
    print(acc.balance)
# chinmay :[34,55,66,777,88]
for acc in accs:
    print(acc.fullName ,acc.lastFiveTransactions())
