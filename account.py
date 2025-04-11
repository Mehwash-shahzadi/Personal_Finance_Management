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

    def calculate_interest(self):
        pass

    def __str__(self):
        return (f"Account(account_id:{self.account_id}, account_name:{self.account_name}, Balance: Rs.{self.balance})")
    

class CheckingAccount(Account):
    def __init__(self, account_id, account_name, balance, created_date, status,overdraft_limit=0):
        super().__init__(account_id, account_name, balance, created_date, status)
        self.overdraft_limit=overdraft_limit
    def withdraw(self, amount):
        if (self.balance - amount) >= (-self.overdraft_limit):
            self.balance-=amount
            print('Rs.' , amount ,'was withdrawn')
            print('total balance=',self.get_balance())
        else:
            print('exceeded the overdraft limit')
    def __str__(self):
        return (f"CheckingAccount(account_id:{self.account_id}, account_name:{self.account_name}, Balance: Rs.{self.balance}),over_draft limit: Rs.{self.overdraft_limit}")


class SavingAccount(Account):
    def __init__(self, account_id, account_name, balance, created_date, status):
        super().__init__(account_id, account_name, balance, created_date, status)