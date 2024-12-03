import re

sum = 0
with open("./inputs/03.txt") as input:
    for line in input:
        matches = re.findall(r'mul\(\d+,\d+\)', line)
        for match in matches:
            match = match[4:-1]
            a, b = match.split(",")
            a, b = int(a), int(b)
            sum += a*b

print(sum)