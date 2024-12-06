map = []
with open("inputs/06.txt") as input:
    for line in input:
        line = line.strip()
        map.append(line)

for y, line in enumerate(map):
    for x, c in enumerate(line):
        if c == "^":
            sx, sy = x, y

map = [[0 if c == "." else 1 for c in line] for line in map]

px, py = sx, sy
direction = "N"

while True:
    if px < 0 or px >= len(map[0]):
        break
    if py < 0 or py >= len(map):
        break

    map[py][px] = -1

    match direction:
        case "N":
            if py > 0 and map[py-1][px] == 1:
                direction = "E"
                continue
            py -= 1
        case "E":
            if px+1 < len(map[0]) and map[py][px+1] == 1:
                direction = "S"
                continue
            px += 1
        case "S":
            if py+1 < len(map) and map[py+1][px] == 1:
                direction  = "W"
                continue
            py += 1
        case "W":
            if px > 0 and map[py][px-1] == 1:
                direction = "N"
                continue
            px -= 1

print(sum([sum([1 for i in line if i < 0]) for line in map]))
