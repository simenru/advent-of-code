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

map = np.zeros(shape=(2*dimx, dimy), dtype=int)
for x, y in np.ndindex((dimx, dimy)):
    c = map_t[y][x]
    match c:
        case "#":
            map[2*x, y] = 8
            map[2*x+1, y] = 8
        case "O":
            map[2*x, y] = 1
            map[2*x+1, y] = 2
        case "@":
            px, py = 2*x, y

print(px, py)

def can_move_ew(px, py, d):
    match map[px+d, py]:
        case 0: #.
            return True
        case 1: #[
            return can_move_ew(px+d, py, d)
        case 2: #]
            return can_move_ew(px+d, py, d)
        case 8: ##
            return False

def can_move_ns(px, py, d):
    match map[px, py+d]:
        case 0: #.
            return True
        case 1: #[
            return can_move_ns(px, py+d, d) and can_move_ns(px+1, py+d, d)
        case 2: #]
            return can_move_ns(px-1, py+d, d) and can_move_ns(px, py+d, d)
        case 8: ##
            return False

def move_ew(px, py, d):
    if map[px, py] == 0:
        return
    if map[px+d, py] != 0:
        move_ew(px+d, py, d)
    map[px+d, py] = map[px, py]
    map[px, py] = 0

def move_ns(px, py, d):
    match map[px, py]:
        case 0: #.
            pass
        case 1: #[
            move_ns(px, py+d, d)
            move_ns(px+1, py+d, d)
            map[px:px+2, py+d] = map[px:px+2, py]
            map[px:px+2, py] = 0
        case 2: #]
            move_ns(px-1, py+d, d)
            move_ns(px, py+d, d)
            map[px-1:px+1, py+d] = map[px-1:px+1, py]
            map[px-1:px+1, py] = 0
            pass
        case 8: ##
            raise ValueError()

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def print_map():
    m = map.copy()
    legend = np.array([".", "[", "]", None, None, None, None, None, "#"])
    m = legend[map]
    m[px, py] = bcolors.FAIL + "@" + bcolors.ENDC
    m = m.T
    for l in list(m):
        print("".join(l))

for line in commands:
    for c in line:
        match c:
            case "^":
                if can_move_ns(px, py, -1):
                    move_ns(px, py-1, -1)
                    py = py-1
            case ">":
                if can_move_ew(px, py, 1):
                    move_ew(px+1, py, 1)
                    px = px+1
            case "v":
                if can_move_ns(px, py, 1):
                    move_ns(px, py+1, 1)
                    py = py+1
            case "<":
                if can_move_ew(px, py, -1):
                    move_ew(px-1, py, -1)
                    px = px-1

score = 0
for x, y in np.ndindex(map.shape):
    if map[x, y] == 1:
        score += x + 100 * y

print_map()
print(score)