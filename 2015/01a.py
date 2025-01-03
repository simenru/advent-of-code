with open("inputs/01.txt") as f:
    data = f.readline()
    data = data.strip()

floor = 0
for c in data:
    match c:
        case "(":
            floor += 1
        case ")":
            floor -= 1

print(floor)