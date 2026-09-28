from storage import load_budget,save_budget,load_expenses
from validators import money_value

def set_budget():
    amount= money_value("Monthly Budget: Rs.")
    save_budget(amount)
    print("Budget saved")

def show_budget():
    budget = load_budget()
    spent = sum(x["amount"] for x in load_expenses())
    print(f"Budget: Rs.{budget:.2f}")    
    print(f"Spent: Rs.{spent:.2f}")    
    print(f"Left: Rs.{budget-spent:.2f}")    