import numpy as np

map_t = []
commands = []

with open("inputs/15.txt") as f:
    reading_map = True
    for line in f:
        line = line.strip()
        if line == "":
            reading_map = False
        
        if reading_map:
            map_t.append(line)
        else:
            commands.append(line)

dimx, dimy = len(map_t[0]), len(map_t)

map = np.zeros(shape=(dimx, dimy), dtype=int)
for x, y in np.ndindex(map.shape):
    c = map_t[y][x]
    match c:
        case "#":
            map[x, y] = 8
        case "O":
            map[x, y] = 1
        case "@":
            px, py = x, y

print(px, py)

def try_move_north(px, py):
    if map[px, py-1] == 0:
        py = py-1
        return px, py
    if map[px, py-1] == 8:
        return px, py
    if map[px, py-1] == 1:
        d = 1
        while map[px, py-d] == 1:
            d += 1
        if map[px, py-d] == 8:
            return px, py
        elif map[px, py-d] == 0:
            map[px, py-d] = 1
            map[px, py-1] = 0
            py = py-1
            return px, py

def try_move_east(px, py):
    if map[px+1, py] == 0:
        px = px+1
        return px, py
    if map[px+1, py] == 8:
        return px, py
    if map[px+1, py] == 1:
        d = 1
        while map[px+d, py] == 1:
            d += 1
        if map[px+d, py] == 8:
            return px, py
        elif map[px+d, py] == 0:
            map[px+d, py] = 1
            map[px+1, py] = 0
            px = px+1
            return px, py

def try_move_south(px, py):
    if map[px, py+1] == 0:
        py = py+1
        return px, py
    if map[px, py+1] == 8:
        return px, py
    if map[px, py+1] == 1:
        d = 1
        while map[px, py+d] == 1:
            d += 1
        if map[px, py+d] == 8:
            return px, py
        elif map[px, py+d] == 0:
            map[px, py+d] = 1
            map[px, py+1] = 0
            py = py+1
            return px, py

def try_move_west(px, py):
    if map[px-1, py] == 0:
        px = px-1
        return px, py
    if map[px-1, py] == 8:
        return px, py
    if map[px-1, py] == 1:
        d = 1
        while map[px-d, py] == 1:
            d += 1
        if map[px-d, py] == 8:
            return px, py
        elif map[px-d, py] == 0:
            map[px-d, py] = 1
            map[px-1, py] = 0
            px = px-1
            return px, py

for line in commands:
    for c in line:
        match c:
            case "^":
                px, py = try_move_north(px, py)
            case ">":
                px, py = try_move_east(px, py)
            case "v":
                px, py = try_move_south(px, py)
            case "<":
                px, py = try_move_west(px, py)

score = 0
for x, y in np.ndindex(map.shape):
    if map[x, y] == 1:
        score += x + 100 * y

print(score)