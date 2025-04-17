def format_currency(amount):
    '''currency formating'''
    return f"${amount:,.2f}"

def format_date(date_obj):
    """date formatting"""
    if date_obj:
        return date_obj.strftime('%b %d,%Y')
    return "Invalid Date"

def calculate_compound_interest(principal, rate, time, compounding_per_year=4):
    """Calculates compound interest."""
    return principal * (1 + rate / compounding_per_year) ** (compounding_per_year * time) - principal

def calculate_loan_amortization(loan_amount, interest_rate, term_years):
    """Calculates the monthly payments."""
    rate_per_month = interest_rate / 12 / 100
    number_of_months = term_years * 12
    return loan_amount * rate_per_month / (1 - (1 + rate_per_month) ** -number_of_months)

def is_positive_number(value):
    'check number is positive'
    return value > 0

def format_title_case(text):
    return text.title()










