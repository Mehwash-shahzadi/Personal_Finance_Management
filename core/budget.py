from datetime import datetime, timedelta,date
class Budget:
    def __init__(self,total_budget,period,spent_amount,start_date=None):
        self.total_budget=total_budget
        self.period=period
        self.spent_amount=spent_amount
        self.start_date=start_date
        self.budget_items=[]
        self.category_limit={}
        self.category_spending={}

        if self.start_date is None:
            self.start_date=date.today()
        else:
            self.start_date=start_date
        self.end_date=self.calculating_end_date()

    def calculating_end_date (self) :
        if self.period=='weekly'  :
            return self.start_date+timedelta(days=7)
        if self.period=='monthly'  :
            return self.start_date+timedelta(days=30)
        if self.period=='annual'  :
            return self.start_date+timedelta(days=365)
        
    def set_category_limit(self,category,limit):
        self.category_limit[category]=limit


    def add_items(self,amount,category,description):
        if amount<0:
            print('amount must be a positive number')
            return
        if  not category or not description:
            print('category and description must be added')
            return
    
        items=BudgetItems(amount,category,description)
        self.budget_items.append(items)
        self.spent_amount+=amount

        self.category_spending[category] = self.category_spending.get(category, 0) + amount 
        if category in self.category_limit:
            if self.category_spending[category] > self.category_limit[category]:
               print('overspending in category')

    
    def category_summary(self):
        for category,spent in self.category_spending.items():
            limit=self.category_limit.get(category,'No Limits')
            print(f'Category:{category},Spent:{spent},limit:{limit}')

    def overspending(self,amount):
        if self.spent_amount+amount>self.total_budget:
            return True
        return False

    def track_budget(self):

        remaining=self.total_budget-self.spent_amount
        remaining_time = self.end_date - datetime.now().date()
        percentage=(self.spent_amount/self.total_budget)*100
        print(f"Remining Budget: ,{remaining}" )
        print(f"Percentage spent:, {percentage}% ")
        print(f"Remaining time:, {remaining_time} ")

 
class BudgetItems:
    def __init__(self,amount,category,description):
        self.amount=amount
        self.category=category
        self.description=description

    def __str__(self):
        return (f'BudgetItems(amount:{self.amount},category:{self.category},description:{self.description})')