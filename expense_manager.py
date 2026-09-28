from storage import load_expenses,save_expenses
from validators import text_value,money_value,id_value
from utils import today, print_expense

def add_expense():
    data = load_expenses()
    item = {
        "id":max([x["id"] for x in data],default=0)+1,
        "date":today(),
        "category": text_value("Category: "),
        "amount": money_value("Amount: Rs."),
        "note": text_value("Note: ")
    }
    data.append(item)
    save_expenses(data)
    print("Expense Added.")

def list_expenses():
    data = load_expenses()
    if not data:
        print("No Expenses Found.")
        return    
    for item in data:
        print_expense(item) 

def delete_expense():
    data = load_expenses()
    item_id = id_value("Expense ID: ")
    new_data = [x for x in data if x["id"] != item_id]
    if len(new_data) ==  len(data):
        print("Expense Not Found.")
    else:
        save_expenses(new_data)
        print("Expense Deleted.")    
