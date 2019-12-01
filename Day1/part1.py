import os, math
script_dir = os.path.dirname(__file__)
input_path = os.path.join(script_dir, 'input.txt')

sum = 0
with open(input_path) as f:
    for x in f.readlines():
        sum += math.floor(int(x) / 3) - 2
    print(sum)