# https://lpuprograms.blogspot.com/2019/02/day-2-operators-in-cpp-or-java-or-python.html

def solve(meal_cost, tip_percent, tax_percent):
    tip = meal_cost * (tip_percent/100)
    tax = meal_cost * (tax_percent/100)
    totalCost = meal_cost + tip + tax
    print(round(totalCost))