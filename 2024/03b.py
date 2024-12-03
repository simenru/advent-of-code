import re

sum = 0
active = True
with open("./inputs/03.txt") as input:
    for line in input:
        matches = re.findall(r"do\(\)|don't\(\)|mul\(\d+,\d+\)", line)
        for match in matches:
            if match == "do()":
                active = True
            elif match == "don't()":
                active = False
            elif active:
                match = match[4:-1]
                a, b = match.split(",")
                a, b = int(a), int(b)
                sum += a*b

print(sum)