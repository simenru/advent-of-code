with open("inputs/01.txt") as f:
    data = f.readline()
    data = data.strip()

floor = 0
for i, c in enumerate(data):
    match c:
        case "(":
            floor += 1
        case ")":
            floor -= 1
    if floor < 0:
        print(i+1)
        exit()
