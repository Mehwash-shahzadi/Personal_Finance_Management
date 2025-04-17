from abc import ABC, abstractmethod
from utility.utils import calculate_loan_amortization,format_currency
class ProjectionCalculator(ABC):
    def __init__(self,initial_amount,rate,time):
        self.initial_amount=initial_amount
        self.rate=rate
        self.time=time

    @abstractmethod
    def projection(self):
        pass

class  SavingsProjection(ProjectionCalculator):
    def __init__(self, initial_amount, rate, time,monthly_contribution):
        super().__init__(initial_amount, rate, time)
        self.monthly_contribution=monthly_contribution

    def projection(self):
        r = self.rate / 100         
        n = 12                      #year compound
        t = self.time
        P = self.initial_amount
        PMT = self.monthly_contribution

        future_value_initial = P * (1 + r/n) ** (n * t)
        future_value_contributions = PMT * (((1 + r/n) ** (n * t) - 1) / (r/n))
        total_future_value=future_value_initial+future_value_contributions
        
        total_contributed = P + (PMT * t * 12)
        interest_earned = total_future_value - total_contributed
        return {
            "initial_amount": round(P, 2),
            "monthly_contribution": round(PMT, 2),
            "total_contributed": round(total_contributed, 2),
            "interest_earned": round(interest_earned, 2),
            "final_savings": round(total_future_value, 2),
            "years": t,
            "annual_rate_percent": self.rate
        }
class DebtProjection(ProjectionCalculator):
    def __init__(self, initial_amount, rate, time,loan_amount,interest_rate,monthly_payment):
        super().__init__(initial_amount, rate, time)
        self.loan_amount=loan_amount
        self.interest_rate=interest_rate
        self.monthly_payment=monthly_payment
    def projection(self):
          calculated_monthly_payment = calculate_loan_amortization(self.loan_amount, self.interest_rate, self.time)
          total_paid= calculated_monthly_payment * 12 * self.time 
          paid_interest_paid= total_paid - self.loan_amount

          return {
           "loan_amount": format_currency(self.loan_amount),
           "monthly_payment": format_currency(calculated_monthly_payment),
           "total_paid": format_currency(total_paid),
           "interest_paid": format_currency(paid_interest_paid),
           "loan_term_years": self.time
          }
class RetirementProjection(ProjectionCalculator):
    def __init__(self, initial_amount, rate, time,monthly_contribution,current_age,retirement_age):
        super().__init__(initial_amount, rate, time)
        self.monthly_contribution=monthly_contribution
        self.current_age=current_age
        self.retirement_age=retirement_age
        

    def projection(self):
        r=self.rate/100
        n=12
        t=self.retirement_age-self.current_age
        P = self.initial_amount
        PMT = self.monthly_contribution
        future_value_initial = P * (1 + r/n) ** (n * t)
        future_value_contributions = PMT * (((1 + r/n) ** (n * t) - 1) / (r/n))
        retirementsaving=future_value_initial+future_value_contributions
        total_contributed = P + (PMT * t * 12)
        interest_earned = retirementsaving - total_contributed


       
        return {
         'final_savings': round(retirementsaving, 2),
         'years_until_retirement': t,
         'total_contributed': round(total_contributed, 2),
         'interest_earned': round(interest_earned, 2)
        }

