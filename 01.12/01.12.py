import math



#First challenge
def calc_fuel(mass):
    return math.floor(mass/3) - 2

#result = sum([calc_fuel(int(line)) for line in open("input.txt").readlines()])

#Second challenge
def calc_fuel_recursive(mass, current_total):
    result = math.floor(mass/3) - 2
    if result <= 0:
        return current_total
    return calc_fuel_recursive(result, current_total + result)

result = sum([calc_fuel_recursive(int(line),0) for line in open("input.txt").readlines()])



print(result)
