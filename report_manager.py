from collections import defaultdict
from storage import load_expenses
from utils import month_now

def monthly_report():
    month = input("Month (YYYY-MM, Enter for current): ").strip() or month_now()
    data = [x for x in load_expenses() if x["date"].startswith(month)]

    if not data:
        print("No expense for this month. ")
        return

    total = sum(x["amount"] for x in data)
    categories = defaultdict(float)

    for item in data:
        categories[item["category"]] += item["amount"]

    print(f"\nReport for {month}")            
    print(f"Total spent: Rs.{total:.2f}")
    for category, amount in categories.items():
        print(f"{category}: Rs.{amount:2f}")            
