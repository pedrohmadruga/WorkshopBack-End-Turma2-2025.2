from math import sqrt

def calc_sqrt():
    try:
        number = int(input("Type a number: "))
    except ValueError:
        return "You did not type a number"
    
    if number < 0:
        return "Negative numbers do not have square root"
    return f"The square root of {number} is {round(sqrt(number), 3)}"

print(calc_sqrt())