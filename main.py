from expense_manager import add_expense,list_expenses,delete_expense
from budget_manager import set_budget,show_budget
from report_manager import monthly_report

def menu():
    print("\n=== STUDENT EXPENSE TRACKER ===")
    print("1. Add Expense")
    print("2. View Expense")
    print("3. Delete Expense")
    print("4. Set Monthly Budget")
    print("5. View Budget")
    print("6. Monthly Report")
    print("0. Exit")

while True:
    menu()
    choice = input("Enter Choice: ")

    if(choice == "1"): 
        add_expense()   
    elif(choice == "2"):
        list_expenses()    
    elif(choice == "3"):
        delete_expense()    
    elif(choice == "4"):
        set_budget()    
    elif(choice == "5"):
        show_budget()    
    elif(choice == "6"):
        monthly_report()    
    elif(choice == "0"):
        print("Thank YOU!") 
        break
    else:
        print("Invalid Choice")   