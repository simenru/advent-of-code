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


class COLORS:
    yellow = "\033[93m"
    red = "\033[91m"
    end = "\033[0m"

def print_map(map, px, py):
    print("----")
    for y, line in enumerate(map):
        line = "".join([str(c) for c in line])
        line = line.replace("0", ".")
        line = line.replace("1", "#")

        if y == py:
            line = line[:x] + COLORS.red + "X" + COLORS.end + line[x+1:]
        print(line)

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
        
        if f"{px},{py},{direction}" in visited:
            return True

count = 0
for y in range(len(map)):
    print(y)
    for x in range(len(map[0])):
        map_copy = [line.copy() for line in map]
        if x != sx or y != sy and map[y][x] != 1:
            map_copy[y][x] = 1
            if is_loop(map_copy, sx, sy, "N"):
                #print(f" {x}, {y}")
                count += 1
                print(f" {count}")
                #print_map(map_copy, sx, sy)
print(count)