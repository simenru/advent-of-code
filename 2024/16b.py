import numpy as np
import heapq

with open("inputs/16.txt") as f:
    data = []
    for line in f:
        line = line.strip()
        data.append(line)

map = np.zeros(shape=(len(data[0]), len(data)))
for x, y in np.ndindex(map.shape):
    match data[y][x]:
        case ".":
            map[x, y] = 0
        case "#":
            map[x, y] = 1
        case "S":
            sx, sy = x, y
        case "E":
            ex, ey = x, y

BEST_DISTANCE = 88468

valid_paths = []
min_length = {}

def step_path(x, y, direction, distance, path: list):
    node = (x, y, direction)
    if node in min_length:
        if min_length[node] < distance:
            return
        elif min_length[node] > distance:
            min_length[node] = distance
    else:
        min_length[node] = distance

    path = path.copy()
    path.append((x, y, direction))

    if x == ex and y == ey:
        if distance == BEST_DISTANCE:
            print(path)
            valid_paths.append(path)
            return
    if distance > BEST_DISTANCE:
        return
    
    match direction:
        case "N":
            step_path(x, y, "E", distance + 1000, path)
            step_path(x, y, "W", distance + 1000, path)
            if map[x, y-1] == 0:
                step_path(x, y-1, "N", distance + 1, path)
        case "S":
            step_path(x, y, "E", distance + 1000, path)
            step_path(x, y, "W", distance + 1000, path)
            if map[x, y+1] == 0:
                step_path(x, y+1, "S", distance + 1, path)
        case "E":
            step_path(x, y, "N", distance + 1000, path)
            step_path(x, y, "S", distance + 1000, path)
            if map[x+1, y] == 0:
                step_path(x+1, y, "E", distance + 1, path)
        case "W":
            step_path(x, y, "N", distance + 1000, path)
            step_path(x, y, "S", distance + 1000, path)
            if map[x-1, y] == 0:
                step_path(x-1, y, "W", distance + 1, path)

step_path(sx, sy, "E", 0, [])

visited = set()

for p in valid_paths:
    for x, y, _ in p:
        visited.add(f"{x},{y}")

print(len(visited))