with open("./inputs/05.txt") as input:
    rules = []
    manuals = []

    for line in input:
        line = line.strip()
        if line == "":
            break
        rules.append(line)
    
    for line in input:
        line = line.strip()
        manuals.append(line)

following = {}
for rule in rules:
    first, second = rule.split("|")
    if not first in following:
        following[first] = {second}
    else:
        following[first].add(second)

sum = 0
for manual in manuals:
    processed = set()
    manual = manual.split(",")
    for key in manual:
        if not processed.isdisjoint(following[key]):
            break
        processed.add(key)
    else:
        sum += int(manual[len(manual)//2])

print(sum)
