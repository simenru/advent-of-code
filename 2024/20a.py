import numpy as np
import heapq

with open("inputs/20.txt") as f:
    data = []
    for line in f:
        line = line.strip()
        data.append(line)

dimx = len(data[0])
dimy = len(data)

map = np.zeros(shape=(dimx, dimy))
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

def time(map, sx, sy, ex, ey):
    distances = {}
    frontier = []
    frontier_distances = {}
    heapq.heapify(frontier)

    def update_node(node, distance):
        if node in distances:
            # Node already visited, so ignor
            return
        x, y = node
        heuristic = distance + abs(x-ex) + abs(y-ey)

        if node in frontier_distances:
            if heuristic < frontier_distances[node]:
                frontier_distances[node] = heuristic
                heapq.heappush(frontier, (heuristic, distance, node))
        else:
            frontier_distances[node] = heuristic
            heapq.heappush(frontier, (heuristic, distance, node))

    update_node((sx, sy), 0)

    while len(frontier) > 0:
        heuristic, distance, node = heapq.heappop(frontier)
        x, y = node
        distances[node] = distance
        if x == ex and y == ey:
            break

        if x > 0 and map[x-1, y] == 0:
            update_node((x-1, y), distance+1)
        if x+1 < dimx and map[x+1, y] == 0:
            update_node((x+1, y), distance+1)
        if y > 0 and map[x, y-1] == 0:
            update_node((x, y-1), distance+1)
        if y+1 < dimy and map[x, y+1] == 0:
            update_node((x, y+1), distance+1)

    return distances[(ex, ey)]

default_time = time(map, sx, sy, ex, ey) # 9336

num_cheats = 0
for x, y in np.ndindex(map.shape):
    if map[x, y] == 1:
        map_c = map.copy()
        map_c[x, y] = 0
        if time(map_c, sx, sy, ex, ey) <= default_time - 100:
            print(x, y)
            num_cheats += 1

print(num_cheats)
exit()

cheats = set()
for x, y in np.ndindex(map.shape):
    if x > 0:
        cheats.add(((x, y), (x-1, y)))
    if x+1 < dimx:
        cheats.add(((x, y), (x+1, y)))
    if y > 0:
        cheats.add(((x, y), (x, y-1)))
    if y+1 < dimy:
        cheats.add(((x, y), (x, y+1)))



num_cheats = 0
for cs, ce in cheats:
    map_c = map.copy()
    map_c[ce[0], ce[1]] = 0
    if time(map_c, sx, sy, ex, ey) <= default_time - 100:
        num_cheats += 1

print(num_cheats) # 1393