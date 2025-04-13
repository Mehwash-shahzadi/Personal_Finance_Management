from core import Account, CheckingAccount, SavingsAccount, CreditAccount
from core import Transaction, Expense, Income, Transfer, search_transaction
from core import Budget
from core import Category
from core import Goal,SavingGoal,DebtPayoffGoal,PurchaseGoal,RetirementGoal
from datetime import date
from core import UserProfile


def main():
    
    #                                           account
    account1 = CheckingAccount(account_id=101, account_name="Mehwash", balance=1000.00, created_date="2025-01-01", status="Active", overdraft_limit=500)
    account2 = SavingsAccount(account_id=102, account_name="Maheen", balance=1000.00, created_date="2025-01-02", status="Active", interest_rate=0.05)
    account3 = CreditAccount(account_id=103, account_name="Maheen", balance=1000.00, created_date="2025-01-02", status="Active", credit_limit=5000, interest_rate=0.05)

    # print(account1)
    # print(account2)
    # print(account3)
    # account1.deposit(1500)
    # account1.withdraw(500)

    #                                         transaction
    transaction1=Expense(transaction_id="T001", date="2025-04-12", amount=500, description="Grocery shopping", category="Food", payee='mishi', recurrence_type=None, next_payment_date=None, end_date=None)
    transaction2=Income(transaction_id="INC001",date="2025-04-01", amount=25000, description="Salary for April", source="ABC Corporation",payee="ABC Corporation",recurrence_type="monthly", next_payment_date="2025-05-01",end_date="2025-12-01")
    transaction3 = Transfer(transaction_id="TRF001",date="2025-04-10",amount=5000,description="Transfer to savings account",to_account="SavingsAccount-Maheen",from_account="CheckingAccount-Mehwash",recurrence_type="monthly",next_payment_date="2025-05-10",end_date="2025-12-10")
    transactions=[transaction1,transaction2,transaction3]
    # print(transaction1)
    # print('next_payment_date:',transaction1.calculate_next_payment_date())
    # print(transaction2)
    # print(transaction3)
    # result=search_transaction(transactions,date="2025-04-01", amount=25000)
    # for t in result:
        # print(t)

     #                                        budget
    # b1=Budget(total_budget=5000,period='monthly',spent_amount=4000,start_date=None)
    # print(b1.total_budget)
    # print(b1.start_date)
    # print(b1.spent_amount)
    # print(b1.end_date)
    # b1.set_category_limit('food',2000)
    # b1.set_category_limit('bills',1000)
    # b1.set_category_limit('travel',300)
    # print(f'spent_amount: {b1.spent_amount}')
    # print(b1.category_limit)
    # b1.add_items(2000,'food','xyz')
    # for item in b1.budget_items:
    #     print(item)
    # if b1.overspending(6000):
    #     print('you are overspending')
    # else:
    #     print('within budget')
    # b1.track_budget()
   

    #                                            Goal
    # my_goal = SavingGoal(goal_name="Emergency Fund",target_amount=10000,current_amount=2000,start_date=date(2024, 1, 1),end_date=date(2025, 12, 31),saving_reason="For medical and urgent needs",monthly_contribution=500)
    # print(my_goal.goal_summary())
    # my_goal.update_progress(2500)
    # my_goal.update_progress(3000)
    # my_goal.update_progress(2500) 

       
    # print(f"Progress: {my_goal.calculate_progress()}%")
    # print(f"Remaining days (estimate): {my_goal.estimate_remaining_time():.2f}")
    # print(f"Is goal completed? {my_goal.is_goal_completed()}")

    #                                         category

    # category1=Category(name='food',id=1)

    # standard_categories =category1.load_standard_categories()
    # print(standard_categories)
    # category1.create_custom_category(parent_id=1,name='chawl',id=3)
    
    # result=category1.search_by_id(id=4)
    # print(result)
    # result=category1.search_by_name('apple')
    # print(result)
    # result=category1.search_by_name_or_id('chines',5)
    # print(result)
    # categories = Category.load_standard_categories()
    # result=categories[0].filter_category_by_id(id=4)
    # print(result)

    #                                     user_profile
    profile1=UserProfile(username='Mehwash', email='mehwash@gmail.com', password='mishi123@', currency='US',locale='en_US')
    print(profile1.username)
    print(profile1.authentication('mishi123@') ) 
    print(profile1.authentication("wrongpassword"))   

    profile1.change_password("newpassword")
    print(profile1.authentication("newpassword"))        



if __name__ == "__main__":
    main()


