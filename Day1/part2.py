import os, math
script_dir = os.path.dirname(__file__)
input_path = os.path.join(script_dir, 'input.txt')

def fuel(mass):
    fuel_needed = math.floor(mass / 3) - 2
    return fuel_needed+fuel(fuel_needed) if fuel_needed > 0 else 0

sum = 0
with open(input_path) as f:
    for x in f.readlines():
        sum += fuel(int(x))
    print(sum)

