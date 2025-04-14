from abc import ABC,abstractmethod
from datetime import datetime
from tabulate import tabulate
from utility.utils import format_currency, format_date

class ReportGenerator(ABC):
    def __init__(self,report_title,start_date,end_date,data):
        self.report_title=report_title
        self.start_date=start_date
        self.end_date=end_date
        self.data=data
    @abstractmethod
    def generate(self):
        pass

class SpendingReport(ReportGenerator):
    def __init__(self, report_title, start_date, end_date, data,category_filter=None):
        super().__init__(report_title, start_date, end_date, data)
        self.category_filter=category_filter
    def generate(self):
        filtered_data=[]
        spent_amount=0
        table_data=[]
        for transaction in self.data:
            transaction_date=datetime.strptime(transaction["date"], "%Y-%m-%d").date()
            if self.start_date<=transaction_date<=self.end_date:
                if self.category_filter is None or transaction['category']==self.category_filter:
                    filtered_data.append(transaction)
                    spent_amount+=transaction['amount']
                    table_data.append([format_date(transaction_date),transaction['category'],format_currency(transaction['amount'])])
        formatted_table = tabulate(table_data, headers=["Date", "Category", "Amount"], tablefmt="fancy_grid")
        return {
            "report_title": self.report_title,
            "total_spent": spent_amount,
            "transactions": filtered_data,
            "category_filter": self.category_filter,
            "start_date": format_date(self.start_date),
            "end_date": format_date(self.end_date),
            "table":formatted_table
            }
    
class BudgetReport(ReportGenerator):
    def __init__(self, report_title, start_date, end_date, data,budget_data):
        super().__init__(report_title, start_date, end_date, data)
        self.budget_data=budget_data
    def generate(self):
        actual_spending={}
        table_data=[]
        for transaction in self.data:
            transaction_date=datetime.strptime(transaction["date"], "%Y-%m-%d").date()
            if self.start_date<=transaction_date<=self.end_date:
                category = transaction["category"]
                amount = transaction["amount"]
                actual_spending[category] = actual_spending.get(category, 0) + amount
                table_data.append([format_date(transaction_date),format_currency(transaction['amount']),transaction['type']])
        formatted_table = tabulate(table_data, headers=["Date", "Amount", "Type"], tablefmt="fancy_grid")
        comparison={}
        for category,budget_amount in self.budget_data.items():
            spent=actual_spending.get(category,0)
            difference=spent-budget_amount
            comparison[category]={
                "budgeted": format_currency(budget_amount),
                "spent": format_currency(spent),
                "difference": format_currency(difference),
                "status": (
                    "Over Budget" if difference > 0
                    else "Under Budget" if difference < 0
                    else "On Budget"
                )
            }
            
        return {
            "report_title": self.report_title,
            "start_date": format_date(self.start_date),
            "end_date": format_date(self.end_date),
            "comparison": comparison,
            "table":formatted_table
        }

class IncomeReport(ReportGenerator):
    def __init__(self, report_title, start_date, end_date, data):
        super().__init__(report_title, start_date, end_date, data)
       
    def generate(self):
        income_transaction=[]
        monthly_income = {}
        table_data=[]
        for transaction in self.data:
            transaction_date=datetime.strptime(transaction['date'],'%Y-%m-%d').date()
            if self.start_date<=transaction_date<=self.end_date and transaction['type']=='income':
                income_transaction.append(transaction)
                month_key=transaction_date.strftime('%Y-%m')
                monthly_income[month_key] = monthly_income.get(month_key, 0) + transaction['amount']
                table_data.append([format_date(transaction_date),format_currency(transaction['amount']),transaction['type']])
        formated_table=tabulate(table_data,headers=["Date","Amount","Type"])


        total_income=sum(monthly_income.values())
        number_of_month=len(monthly_income)
        average_income=total_income/number_of_month if number_of_month > 0 else 0

        return {
         "report_title": self.report_title,
         "start_date": format_date(self.start_date),
         "end_date": format_date(self.end_date),
         "monthly_income": monthly_income,
         "total_income": format_currency(total_income),
         "income_transaction":income_transaction,
         "average_income": format_currency(average_income),
         "table":formated_table
        }
    
class NetWorthReport(ReportGenerator):
    def __init__(self, report_title, start_date, end_date, data,assets,debts):
        super().__init__(report_title, start_date, end_date, data)
        self.assets=assets
        self.debts=debts

    def generate(self):
        total_income=0
        total_expense=0
        for transaction in self.data:
            transaction_date=datetime.strptime(transaction['date'],'%Y-%m-%d').date()
            if self.start_date<=transaction_date<=self.end_date:
                if transaction['type']=='income':
                    total_income+=transaction['amount']
                if transaction['type']=='expense':
                    total_expense+=transaction['amount']
        total_assets=sum(self.assets.values())
        total_debts=sum(self.debts.values())
        net_worth=(total_income-total_expense)+(total_assets-total_debts)

        return {
        "report_title": self.report_title,
         "start_date": format_date(self.start_date),
         "end_date": format_date(self.end_date),
         "total_income": format_currency(total_income),
         "total_expense": format_currency(total_expense),
         "total_assets": format_currency(total_assets),
         "total_debts": format_currency(total_debts),
         "net_Wort": net_worth
        }
    



