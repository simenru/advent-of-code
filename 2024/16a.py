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

distances = {}
frontier = []
frontier_distances = {}
heapq.heapify(frontier)

def update_node(node, distance):
    if node in distances:
        # Node already visited, so ignore
        return
    x, y, _ = node
    heuristic = distance + abs(x-ex) + abs(y-ey)

    if node in frontier_distances:
        if heuristic < frontier_distances[node]:
            frontier_distances[node] = heuristic
            heapq.heappush(frontier, (heuristic, distance, node))
    else:
        frontier_distances[node] = heuristic
        heapq.heappush(frontier, (heuristic, distance, node))

update_node((sx, sy, "E"), 0)

while len(frontier) > 0:
    heuristic, distance, node = heapq.heappop(frontier)
    x, y, direction = node
    distances[node] = distance
    if x == ex and y == ey:
        break

    match direction:
        case "N":
            update_node((x, y, "E"), distance+1000)
            update_node((x, y, "W"), distance+1000)
            if map[x, y-1] == 0:
                update_node((x, y-1, "N"), distance+1)
        case "S":
            update_node((x, y, "E"), distance+1000)
            update_node((x, y, "W"), distance+1000)
            if map[x, y+1] == 0:
                update_node((x, y+1, "S"), distance+1)
        case "E":
            update_node((x, y, "N"), distance+1000)
            update_node((x, y, "S"), distance+1000)
            if map[x+1, y] == 0:
                update_node((x+1, y, "E"), distance+1)
        case "W":
            update_node((x, y, "N"), distance+1000)
            update_node((x, y, "S"), distance+1000)
            if map[x-1, y] == 0:
                update_node((x-1, y, "W"), distance+1)

for dir in ["N","S","E","W"]:
    node = (ex, ey, dir)
    if node in distances:
        print(distances[node])