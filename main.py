from core import Account, CheckingAccount, SavingsAccount, CreditAccount
from core import Transaction, Expense, Income, Transfer, search_transaction
from core import Budget
from core import Category
from core import Goal,SavingGoal,DebtPayoffGoal,PurchaseGoal,RetirementGoal
from datetime import date,datetime
from core import UserProfile

from services import ReportGenerator,SpendingReport,IncomeReport,NetWorthReport
from services import NotificationManager,BudgetAlert,ScheduledNotification,GoalReminder

from data import DataManager
from ui import ConsoleUi


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
    # profile1=UserProfile(username='Mehwash', email='mehwash@gmail.com', password='mishi123@', currency='US',locale='en_US')
    # print(profile1.username)
    # print(profile1.authentication('mishi123@') ) 
    # print(profile1.authentication("wrongpassword"))   

    # profile1.change_password("newpassword")
    # print(profile1.authentication("newpassword"))        

 

    # transactions = [
    #     {"amount": 50, "date": "2024-04-01", "category": "food"},
    #     {"amount": 30, "date": "2024-04-02", "category": "transport"},
    #     {"amount": 20, "date": "2024-04-05", "category": "food"},
    #       ]

    # start_date = datetime.strptime("2024-04-01", "%Y-%m-%d").date()
    # end_date = datetime.strptime("2024-04-10", "%Y-%m-%d").date()

    # report = SpendingReport("Food Expenses Report", start_date, end_date, transactions, category_filter="food")
    # result = report.generate()

    # print(result['table'])
                         
    # transactions = [
    #     {"amount": 10000, "date": "2024-01-15", "type": "income"},
    #     {"amount": 12000, "date": "2024-02-15", "type": "income"},
    #     {"amount": 9000, "date": "2024-03-10", "type": "income"},
    #     {"amount": 3000, "date": "2024-03-25", "type": "income"},
    #     {"amount": 1500, "date": "2024-03-05", "type": "expense"}, 
    #       ]
    # start_date = datetime.strptime("2024-01-01", "%Y-%m-%d").date()
    # end_date = datetime.strptime("2024-03-31", "%Y-%m-%d").date()
    # report = IncomeReport("Quarterly Income Report", start_date, end_date, transactions)
    # result = report.generate()
    # print(result['table'])


        # Sample Transactions (Income and Expenses)
    # data = [
    #     {"date": "2024-04-01", "type": "income", "amount": 10000},
    #     {"date": "2024-04-05", "type": "expense", "amount": 5000},
    #     {"date": "2024-04-10", "type": "income", "amount": 15000},
    #     {"date": "2024-04-15", "type": "expense", "amount": 7000},
    #    ]
    # assets = {
    #   "bank_balance": 100000,
    #   "car": 50000,
    #   "house": 300000,
    # }
    # debts = {
    #   "loan": 100000,
    #   "credit_card": 50000,
    # }
    # report_title = "Net Worth Report for April 2024"
    # start_date = datetime.strptime("2024-04-01", "%Y-%m-%d").date()
    # end_date = datetime.strptime("2024-04-30", "%Y-%m-%d").date()

    # report = NetWorthReport(report_title, start_date, end_date, data, assets, debts)
    # result = report.generate()
    # print(result)

#                          notificationmanager

    # nm = NotificationManager()

    # nm.add_notification(BudgetAlert("Food", 500, 460))
    # nm.add_notification(GoalReminder("Emergency Fund", 1000, 750))
    # nm.add_notification(ScheduledNotification("Don't forget to review your budget!", "weekly", "Monday"))

    # nm.send_all()

#                        DataManager

 

    # dm = DataManager.get_instance()
    # dm.validate_data()

    # dm.add_goal("Save for new laptop")
    # dm.add_alert("Monthly food budget near limit")
    # dm.add_notification("Reminder: Rent is due tomorrow!")

    # dm.save_to_file()

    # dm.load_from_file()

    # dm.create_backup()

    # dm.export_data("data/exported_data.json")

    # dm.import_data("data/backup_data.json")
    # print("Current Data:")
    # print(dm.get_all_data())

    ui = ConsoleUi()
    ui.start_ui()






if __name__ == "__main__":
    main()  


