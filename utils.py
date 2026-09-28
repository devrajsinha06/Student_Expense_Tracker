from datetime import date

def today():
    return str(date.today())

def month_now():
    return today()[:7]

def print_expense(item):
    print(
        f'{item["id"]}.{item["date"]} |'
        f'{item["category"]:<12} | Rs.{item["amount"]:.2f} |'
        f'{item["note"]}'
    )        