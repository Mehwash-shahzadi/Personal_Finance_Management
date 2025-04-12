from datetime import datetime, timedelta

class Transaction:
    def __init__(self, transaction_id, date, amount, description, metadata=None, recurrence_type=None, next_payment_date=None, end_date=None):
        self.transaction_id = transaction_id
        self.date = self.parse_date(date)
        self.amount = amount
        self.description = description
        self.metadata = metadata if metadata is not None else {'tags':[] ,'labels':[]}
        self.recurrence_type = recurrence_type
        self.next_payment_date = self.parse_date(next_payment_date) if next_payment_date else self.date
        self.end_date = self.parse_date(end_date) if end_date else None 

    def __str__(self):
        return (f'Transaction(transaction_id:{self.transaction_id}, Date:{self.date}, Amount:{self.amount}, Description:{self.description}, '
                f'Recurrence Type:{self.recurrence_type}, Next Payment Date:{self.next_payment_date}, End Date:{self.end_date})')
          

    def add_tag(self,tag):
        self.metadata['tags'].append(tag)
    def add_label(self,label):
        self.metadata['labels'].append(label)

    def calculate_next_payment_date(self):
        '''transfering recurring management'''
        if self.recurrence_type == 'monthly':
            new_month = self.next_payment_date.month + 1 if self.next_payment_date.month < 12 else 1
            new_year = self.next_payment_date.year if self.next_payment_date.month < 12 else self.next_payment_date.year + 1
            self.next_payment_date = self.next_payment_date.replace(year=new_year, month=new_month)
        elif self.recurrence_type == 'weekly':
            self.next_payment_date += timedelta(weeks=1)
        elif self.recurrence_type == 'daily':
            self.next_payment_date += timedelta(days=1)
        elif self.recurrence_type == 'yearly':
            self.next_payment_date = self.next_payment_date.replace(year=self.next_payment_date.year + 1)

        if self.end_date and self.next_payment_date > self.end_date:
            return None  
        return self.next_payment_date

    def parse_date(self, date_str):
        '''Date handling'''
        try:
            return datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError("Date must be in YYYY-MM-DD format")
        
    def search_crietria(self, date=None, amount=None, payee=None):
        if date:
           if isinstance(date, str):
            date = self.parse_date(date)
           if self.date == date:
            return True

        if amount and self.amount == amount:
            return True

        if payee and hasattr(self, 'payee') and self.payee == payee:
            return True

        return False

   
    

class Expense(Transaction):
    def __init__(self, transaction_id, date, amount, description, category, payee, recurrence_type=None, next_payment_date=None, end_date=None):
        super().__init__(transaction_id, date, amount, description, recurrence_type=recurrence_type, next_payment_date=next_payment_date, end_date=end_date)
        self.category = category
        self.payee = payee

    def expense_detail(self):
        pass


class Income(Transaction):
    def __init__(self, transaction_id, date, amount, description, source, payee, recurrence_type=None, next_payment_date=None, end_date=None):
        super().__init__(transaction_id, date, amount, description, recurrence_type=recurrence_type, next_payment_date=next_payment_date, end_date=end_date)
        self.source = source
        self.payee = payee

    def income_detail(self):
        pass

class Transfer(Transaction):
    def __init__(self, transaction_id, date, amount, description, to_account, from_account, recurrence_type=None, next_payment_date=None, end_date=None):
        super().__init__(transaction_id, date, amount, description, recurrence_type=recurrence_type, next_payment_date=next_payment_date, end_date=end_date)
        self.to_account = to_account
        self.from_account = from_account

    def transfer_detail(self):
        pass

def search_transaction(transactions,date=None,amount=None,payee=None):
    matching_transaction=[]
    for transaction in transactions:
        if transaction.search_crietria(date=date, amount=amount, payee=payee):
            matching_transaction.append(transaction)
    return matching_transaction




