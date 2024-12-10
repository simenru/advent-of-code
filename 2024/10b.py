with open("inputs/10.txt") as input:
    data = []
    for line in input:
        data.append(line.strip())
    map = [[int(c) for c in line] for line in data]

def score(x, y):
    if map[y][x] == 9:
        return 1
    next_elevation = map[y][x] + 1
    sum = 0
    if x-1 >= 0 and map[y][x-1] == next_elevation:
        sum += score(x-1, y)
    if x+1 < len(map[0]) and map[y][x+1] == next_elevation:
        sum += score(x+1, y)
    if y-1 >= 0 and map[y-1][x] == next_elevation:
        sum += score(x, y-1)
    if y+1 < len(map) and map[y+1][x] == next_elevation:
        sum += score(x, y+1)
    return sum


sum = 0
for y in range(len(map)):
    for x in range(len(map[0])):
        if map[y][x] == 0:
            s = score(x, y)
            print(x, y, s)
            sum += s

print(sum)