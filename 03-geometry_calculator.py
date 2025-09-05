from math import pi as PI, sqrt, pow

class Calculator:
    def calc_circle_area(radius):
        return round(PI * radius * radius, 3)

    def calc_triangle_area(base, height):
        return round(base * height / 2, 3)

    def calc_hypotenuse(a, b):
        return round(sqrt(pow(a, 2) + pow(b, 2)), 3)

def calculator():
    print("1. Calc circle area given radius")
    print("2. Calc triangle area given base and height")
    print("3. Calc hypotenuse given cathets")
    
    try:
        choice = int(input("Choose an option: "))
    except ValueError:
        return "You did not type a number"
    
    match choice:
        case 1:
            try:
                radius = float(input("Insert radius: "))
            except ValueError:
                return("Error: input was not a number")
            
            return Calculator.calc_circle_area(radius)
        case 2:
            try:
                base = float(input("Insert base: "))
                height = float(input("Insert height: "))
            except ValueError:
                return("Error: input was not a number")
            
            return Calculator.calc_triangle_area(base, height)
        case 3:
            try:
                cathet1 = float(input("Insert first cathet: "))
                cathet2 = float(input("Insert second cathet: "))
            except ValueError:
                return("Error: input was not a number")
            
            return Calculator.calc_hypotenuse(cathet1, cathet2)
        case _:
            return "Option not available"

print(calculator())