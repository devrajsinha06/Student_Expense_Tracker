import unittest
from pathlib import Path
from storage import save_expenses,load_expenses,save_budget,load_budget

class TestProject(unittest.TestCare):
    def test_expense_storage(self):
        data = [{"id":1,"date":"2026-09-01",
                "category":"Food","amount":100,"note":"Lunch"}]
        save_expenses(data)
        self.assertEqual(load_expenses(),data)

    def test_budget_storage(self):
        save_budget(5000)
        self.assertEqual(load_budget(),5000)

if __name__ == "__main__":
    unittest.main()                 