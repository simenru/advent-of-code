import numpy as np
import heapq

map = np.zeros(shape=(71, 71), dtype=int)

with open("inputs/18.txt") as f:
    count = 0
    for line in f:
        line = line.strip()
        x, y = line.split(",")
        x, y = int(x), int(y)
        map[x, y] = 1
        count += 1
        if count >= 1024:
            break

sx, sy = 0, 0
ex, ey = 70, 70


distances = {}
frontier = []
frontier_distances = {}
heapq.heapify(frontier)

def update_node(node, distance):
    if node in distances:
        # Node already visited, so ignore
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
    if x+1 < 71 and map[x+1, y] == 0:
        update_node((x+1, y), distance+1)
    if y > 0 and map[x, y-1] == 0:
        update_node((x, y-1), distance+1)
    if y+1 < 71 and map[x, y+1] == 0:
        update_node((x, y+1), distance+1)

print(distances)