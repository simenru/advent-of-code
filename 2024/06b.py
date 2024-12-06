map = []
with open("inputs/06.txt") as input:
    for line in input:
        line = line.strip()
        map.append(line)

for y, line in enumerate(map):
    for x, c in enumerate(line):
        if c == "^":
            sx, sy = x, y

map = [[1 if c == "#" else 0 for c in line] for line in map]

def step(map, px, py, direction) -> tuple[int, int, str]:
    match direction:
        case "N":
            if py > 0 and map[py-1][px] == 1:
                return px, py, "E"
            return px, py-1, direction
        case "E":
            if px+1 < len(map[0]) and map[py][px+1] == 1:
                return px, py, "S"
            return px+1, py, direction
        case "S":
            if py+1 < len(map) and map[py+1][px] == 1:
                return px, py, "W"
            return px, py+1, "S"
        case "W":
            if px > 0 and map[py][px-1] == 1:
                return px, py, "N"
            return px-1, py, "W"

def visited_cells(map, sx, sy, sdir) -> set[tuple[int, int]]:
    px, py, direction = sx, sy, sdir
    visited = set()
    while True:
        if px < 0 or px >= len(map[0]):
            break
        if py < 0 or py >= len(map):
            break
        
        px, py, direction = step(map, px, py, direction)
        visited.add((px, py))
    return visited
    

def is_loop(map, sx, sy, sdir):
    px, py = sx, sy
    direction = sdir    
    visited = set()
    while True:
        visited.add(f"{px},{py},{direction}")

        if px < 0 or px >= len(map[0]):
            return False
        if py < 0 or py >= len(map):
            return False
        
        px, py, direction = step(map, px, py, direction)
        
        if f"{px},{py},{direction}" in visited:
            return True

count = 0
for x, y in visited_cells(map, sx, sy, "N"):
    if x < 0 or x >= len(map[0]):
        continue
    if y < 0 or y >= len(map):
        continue
    map_copy = [line.copy() for line in map]
    if x != sx or y != sy and map[y][x] != 1:
        map_copy[y][x] = 1
        if is_loop(map_copy, sx, sy, "N"):
            count += 1

print(count)