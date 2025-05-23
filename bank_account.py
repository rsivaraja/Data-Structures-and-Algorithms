class bankaccount():
    def __init__(self,accountname,balance,banknumber):
        self.accountname=accountname
        self.balance=balance
        self.banknumber=banknumber
    
    def deposit(self):
        deposit=float(input('How much would you like to deposit?'))
        self.balance+=deposit
        print('Your deposit has been successful.')
    
    def withdraw(self):
        withdrawal=float(input('How much would you like to withdraw?'))
        if withdrawal<=self.balance:
            self.balance-=withdrawal
            print('Your withdrawal has been successful.')
        else:
            print('Not enough money in balance to withdraw.')

    def display_balance(self):
        print(self.balance)
    
    def display_account(self):
        print(f'Account name: {self.accountname}')
        print(f'Balance: ${self.balance}')
        print(f'Bank number: {self.banknumber}')

b1=bankaccount('riasiv',21324747357894983598,12345678)
b2=bankaccount('shivk',192837465,56712)

class studentaccounts(bankaccount):
    def __init__(self,accountname,balance,banknumber,age,guardian_name):
        super().__init__(accountname,balance,banknumber)
        self.age=age
        self.guardian_name=guardian_name
    
    def student_discount(self):
        if self.age<=18:
            print(f'You have access to a 30% discount if you want to take a loan')
        else:
            print('You are not subject to a discount for your loans as you do not meet the requirements.')

s1=studentaccounts('riasi',17285436,6549,15,'kavita')
# s1.student_discount()
# s1.withdraw()

class elderlyaccounts(bankaccount):
    def __init__(self,accountname,balance,banknumber,age):
        super().__init__(accountname,balance,banknumber)
        self.age=age

    def elderly_discount(self):
        if self.age>=67:
            print(f'You have access to a 40% discount for any loan taken.')
        else:
            print('You are not subject to this discount as you do not meet the requirements.')
    
e1=elderlyaccounts('ririri',51671546,6497,66)
e1.elderly_discount()
e1.display_account()