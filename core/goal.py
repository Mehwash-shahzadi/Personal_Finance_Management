from datetime import datetime,date
class Goal:
    def __init__(self,goal_name,target_amount,current_amount,start_date,end_date):
        self.goal_name=goal_name
        self.target_amount=target_amount
        self.current_amount=current_amount
        self.start_date=start_date
        self.end_date=end_date
        self.reached_75 = False

    
    def update_progress(self,amount):
        '''progress updation based on the current amount'''
        if amount>0:
            self.current_amount+=amount
            if self.current_amount>self.target_amount:
                self.current_amount=self.target_amount
                print('you reach the goal!')

            self.check_milestone()
        else:
            print('amount will be in positive number!')

    def calculate_progress(self):
        '''progress in percentage'''
        if self.target_amount!=0:
            result=((self.current_amount)/(self.target_amount))*100
            return round(result,2)
        else:
            return 0
        
    def estimate_remaining_time(self):
        '''timeline estimation'''
        days_passed=(date.today()-self.start_date).days

        if days_passed>0:
            average_saving_per_day=self.current_amount/days_passed
        else:
            average_saving_per_day=0
        remaining_amount=self.target_amount-self.current_amount
        if average_saving_per_day > 0:
             remaining_days = remaining_amount / average_saving_per_day
        else:
             remaining_days = 0
        return remaining_days

    
    def is_goal_completed(self):
        '''goal completion'''
        if self.current_amount>=self.target_amount:
            return True
        return False
    
    def goal_summary(self):
        return (f'name_of_goal:{self.goal_name},Target_amount:{self.target_amount},current_amount:{self.current_amount},start_date:{self.start_date},end_date:{self.end_date}')
    
    def check_milestone(self):
        '''summary of goal'''
        percent = self.calculate_progress()
        if percent >= 75 and not self.reached_75:
           print(" You've reached 75% of your goal!")
           self.reached_75 = True
        if percent==100:
            print("Congratulation's!,you have reached your goal")


class SavingGoal(Goal):
    def __init__(self, goal_name, target_amount, current_amount, start_date, end_date,saving_reason,monthly_contribution ):
        super().__init__(goal_name, target_amount, current_amount, start_date, end_date)
        self.saving_reason=saving_reason
        self.monthly_contribution=monthly_contribution


class DebtPayoffGoal(Goal):
    def __init__(self, goal_name, target_amount, current_amount, start_date, end_date,debt_type,interest_rate,minimum_payment):
        super().__init__(goal_name, target_amount, current_amount, start_date, end_date)
        self.debt_type=debt_type
        self.interest_rate=interest_rate
        self.minimum_payment=minimum_payment

class PurchaseGoal(Goal):
    def __init__(self, goal_name, target_amount, current_amount, start_date, end_date,item_name,priority_level):
        super().__init__(goal_name, target_amount, current_amount, start_date, end_date)
        self.item_name=item_name
        self.priority_level=priority_level

class RetirementGoal(Goal):
    def __init__(self, goal_name, target_amount, current_amount, start_date, end_date,retirement_age,expected_monthly_expenses):
        super().__init__(goal_name, target_amount, current_amount, start_date, end_date)
        self.retirement_age=retirement_age
        self.expected_monthly_expenses=expected_monthly_expenses