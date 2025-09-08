from math import ceil, floor

def round_number():
    try:
        number = float(input("Type a number: "))
    except ValueError:
        return "You did not type a number"
    
    return f"\nRounding up: ${ceil(number)}\nRounding down: ${floor(number)}\nSmart rounding: ${round(number)}"

print(round_number())