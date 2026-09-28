def text_value(message):
    while True:
        value = input(message).strip()
        if value:
            return value
        print("Value cannot be empty.")

def money_value(message):
    while True:
        try:
            value = float(input(message))
            if value > 0:
                return value
        except ValueError:
            pass
        print("Enter a positive number.")

def id_value(message):
    while True:
        try:
            value = int(input(message))
            if value > 0:
                return value
        except ValueError:
                pass
                print("Enter a valid number.")                            