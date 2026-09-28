import json
from pathlib import Path

FILE = Path("data/expenses.json")
BUDGET_FILE = Path("data/budget.json")

def load_expenses():
    if not FILE.exists():
        return []
    return json.loads(FILE.read_text())

def save_expenses(data):
    FILE.parent.mkdir(exist_ok=True)
    FILE.write_text(json.dumps(data, indent=4))

def load_budget():
    if not BUDGET_FILE.exists():
        return 0 
    return json.loads(BUDGET_FILE.read_text()).get("budget",0)

def save_budget(amount):
    BUDGET_FILE.parent.mkdir(exist_ok=True)
    BUDGET_FILE.write_text(json.dumps({"budget": amount},indent=4))                    
    