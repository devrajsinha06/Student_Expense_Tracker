# Student Expense Tracker - Project Report

## 1. Cover Page
**Project:** Student Expense Tracker  
**Student:** Dev Raj Sinha  
**Registration No.:** 26BAI10050  
**Course:** B.Tech(AI & ML)
**Date:** 28/09/2026

## 2. Introduction
Student Expense Tracker is a Python command-line application that helps students record expenses, manage a monthly budget and understand spending patterns.

## 3. Problem Statement
Students need a simple way to record daily expenses and compare spending with a planned budget.

## 4. Objectives
- Record expenses accurately.
- Store expense information permanently.
- Allow deletion of incorrect records.
- Set and view a monthly budget.
- Generate category-wise monthly reports.
- Demonstrate modular Python programming.

## 5. Functional Requirements
### FR1 - Expense Management
The user can add, view and delete expenses.

### FR2 - Budget Management
The user can set a budget and view budget, spending and remaining amount.

### FR3 - Reporting
The system can calculate monthly total spending and category-wise spending.

### FR4 - Data Storage
The system stores records in JSON files.

## 6. Non-Functional Requirements
### Usability
The menu and prompts should be simple for a beginner.

### Performance
For normal student-sized data, operations should complete quickly.

### Reliability
Data is saved after expense and budget changes.

### Maintainability
The program is divided into small Python modules.

### Error Handling
Invalid numbers and empty input are rejected.

### Resource Efficiency
The project uses lightweight local JSON files and Python standard-library modules.

## 7. System Architecture

User
  |
  v
main.py
  |
  +--> expense_manager.py
  |
  +--> budget_manager.py
  |
  +--> report_manager.py
  |
  v
storage.py
  |
  +--> expenses.json
  |
  +--> budget.json

## 8. Workflow Diagram

Start
  |
Show Menu
  |
Choose Operation
  |
  +--> Add/View/Delete Expense
  |
  +--> Set/View Budget
  |
  +--> Monthly Report
  |
Save/Read Data
  |
Return to Menu
  |
Exit

## 9. Use Case Diagram

Student --> Add Expense
Student --> View Expenses
Student --> Delete Expense
Student --> Set Budget
Student --> View Budget
Student --> Generate Monthly Report

## 10. Sequence Diagram

Student -> main.py: Select option
main.py -> module: Call operation
module -> storage.py: Read/Write JSON
storage.py -> module: Return data
module -> main.py: Result
main.py -> Student: Display result

## 11. Component/Class Design

main.py
  |
  +-- Expense Manager
  +-- Budget Manager
  +-- Report Manager
  +-- Storage
  +-- Validators
  +-- Utilities

## 12. Data/Storage Design

### expenses.json
Each expense contains:
- id
- date
- category
- amount
- note

### budget.json
Contains:
- budget

Simple relationship:
One student can create many expense records.

## 13. Design Decisions and Rationale
Python was selected because it is the main implementation language and supports modular programming and file handling through its standard library. JSON was selected because it is simple to read and write and does not require an external database.

## 14. Implementation Details
The application uses separate modules for expenses, budget operations, reporting, validation and storage. The main file controls the menu. JSON files provide persistent local storage.

## 15. Screenshots / Results
Take screenshots of:
1. Main menu
2. Adding an expense
3. Viewing expenses
4. Budget result
5. Monthly report
6. Test result

Paste the screenshots here before exporting this report to PDF.

## 16. Testing Approach
Unit tests are included in `test_project.py`.

Test 1: Save and load an expense.
Expected: Loaded data equals saved data.

Test 2: Save and load a budget.
Expected: Loaded budget equals saved budget.

Run:
`python -m unittest test_project.py`

## 17. Challenges Faced
- Designing a simple menu workflow.
- Validating user input.
- Maintaining data between program runs.
- Dividing the program into small modules.

## 18. Learnings and Key Takeaways
- Python functions and modules
- JSON file handling
- Input validation
- Basic software architecture
- Unit testing
- GitHub project organization
- Technical documentation

## 19. Future Enhancements
- Edit an existing expense
- Search expenses by category
- Add charts
- Add login support
- Export reports to CSV
- Add a graphical interface

## 20. References
- VITyarthi Build Your Own Project guidelines
- Python Standard Library documentation
