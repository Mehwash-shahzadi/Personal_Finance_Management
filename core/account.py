class Account:
    def __init__(self,account_id,account_name,balance,created_date,status):
        self.account_id=account_id
        self.account_name=account_name
        self.balance=balance
        self.created_date=created_date
        self.status=status
        self.transactions = []


    def deposit(self,amount):
        self.balance+=amount
        print('Rs.' , amount ,'was deposit')
        print('total balance=',self.get_balance())

    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
            print('Rs.' , amount ,'was withdraw')
            print('total balance=',self.get_balance())
        else:
            print('Insufficient balance')

    def get_balance(self):
        return self.balance

    def add_transaction(self, transaction):
        self.transactions.append(transaction)


    def __str__(self):
        return (f"Account(account_id:{self.account_id}, account_name:{self.account_name}, Balance: Rs.{self.balance})")
    

class CheckingAccount(Account):
    def __init__(self, account_id, account_name, balance, created_date, status,overdraft_limit =0):
        super().__init__(account_id, account_name, balance, created_date, status)
        self.overdraft_limit= overdraft_limit
    def withdraw(self, amount):
        if (self.balance - amount) >= (-self.overdraft_limit):
            self.balance-=amount
            print('Rs.' , amount ,'was withdrawn')
            print('total balance=',self.get_balance())
        else:
            print('exceeded the overdraft limit')
    def __str__(self):
        return (f"CheckingAccount(account_id:{self.account_id}, account_name:{self.account_name}, Balance: Rs.{self.balance}),over_draft limit: Rs.{self.overdraft_limit}")


class SavingsAccount(Account):
    def __init__(self, account_id, account_name, balance, created_date, status,interest_rate):
        super().__init__(account_id, account_name, balance, created_date, status)
        self.interest_rate=interest_rate

    def withdraw(self, amount):
        return super().withdraw(amount)
    
    def deposit(self, amount):
        return super().deposit(amount)
    
    def calculate_interest(self):
        interest=self.balance*self.interest_rate
        self.balance+=interest
        return interest
        
    def get_balance(self):
        return super().get_balance()
    
    def __str__(self):
        return (f"SavingAccount(account_id:{self.account_id}, account_name:{self.account_name}, Balance: Rs.{self.balance}),creates_date:{self.created_date},status:{self.status},interest_rate: Rs.{self.interest_rate}")
    
class CreditAccount(Account):
    def __init__(self, account_id, account_name, balance, created_date, status,credit_limit,interest_rate):
        super().__init__(account_id, account_name, balance, created_date, status)
        self.credit_limit=credit_limit
        self.interest_rate=interest_rate

    def charge(self,amount):
        if self.balance + amount<=self.credit_limit:
           self.balance+=amount
        else:
            print('exceeded the credit card limit')

    def make_payment(self,amount):
        self.balance-=amount

    def get_balance(self):
        return super().get_balance()
    
    def calculate_interest(self):
        interest=self.balance*self.interest_rate
        self.balance+=interest
        return interest

    def credit_card_limit(self):
        return self.credit_limit
    
    def __str__(self):
        return (f"CreditAccount(account_id:{self.account_id}, account_name:{self.account_name}, Balance: Rs.{self.balance}),credit_limit: Rs.{self.credit_limit},interest_rate:{self.interest_rate}")