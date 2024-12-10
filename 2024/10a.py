with open("inputs/10.txt") as input:
    data = []
    for line in input:
        data.append(line.strip())
    map = [[int(c) for c in line] for line in data]

def score(x, y, visited: set):
    visited.add(f"{x},{y}")
    if map[y][x] == 9:
        return 1
    next_elevation = map[y][x] + 1
    sum = 0
    if x-1 >= 0 and map[y][x-1] == next_elevation and f"{x-1},{y}" not in visited:
        sum += score(x-1, y, visited)
    if x+1 < len(map[0]) and map[y][x+1] == next_elevation and f"{x+1},{y}" not in visited:
        sum += score(x+1, y, visited)
    if y-1 >= 0 and map[y-1][x] == next_elevation and f"{x},{y-1}" not in visited:
        sum += score(x, y-1, visited)
    if y+1 < len(map) and map[y+1][x] == next_elevation and f"{x},{y+1}" not in visited:
        sum += score(x, y+1, visited)
    return sum


sum = 0
for y in range(len(map)):
    for x in range(len(map[0])):
        if map[y][x] == 0:
            s = score(x, y, set())
            sum += s

print(sum) # 682