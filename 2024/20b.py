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

def calculate_distances(map, sx, sy):
    distances = {}
    frontier = []
    frontier_distances = {}
    heapq.heapify(frontier)

    def update_node(node, distance):
        if node in distances:
            # Node already visited, so ignore
            return
        x, y = node

        if node in frontier_distances:
            if distance < frontier_distances[node]:
                frontier_distances[node] = distance
                heapq.heappush(frontier, (distance, node))
        else:
            frontier_distances[node] = distance
            heapq.heappush(frontier, (distance, node))

    update_node((sx, sy), 0)

    while len(frontier) > 0:
        distance, node = heapq.heappop(frontier)
        x, y = node
        distances[node] = distance
        
        if x > 0 and map[x-1, y] == 0:
            update_node((x-1, y), distance+1)
        if x+1 < dimx and map[x+1, y] == 0:
            update_node((x+1, y), distance+1)
        if y > 0 and map[x, y-1] == 0:
            update_node((x, y-1), distance+1)
        if y+1 < dimy and map[x, y+1] == 0:
            update_node((x, y+1), distance+1)

    return distances

distance_from_start = calculate_distances(map, sx, sy)
distance_from_goal = calculate_distances(map, ex, ey)

base_distance = distance_from_start[(ex, ey)]

max_cheat_length = 20
min_time_save = 100

cheat_count = 0
for csx, csy in np.ndindex(map.shape):
    if map[csx, csy] == 1:
        # Cannot start in wall
        continue
    distance_to_start = distance_from_start[(csx, csy)]
    for cex, cey in np.ndindex(map.shape):
        if map[cex, cey] == 1:
            # Cannot end in wall
            continue

        length = abs(csx - cex) + abs(csy - cey)
        if length > max_cheat_length:
            continue
        
        distance_to_goal = distance_from_goal[(cex, cey)]

        time = distance_to_start + length + distance_to_goal
        if time <= base_distance - 100:
            cheat_count += 1

print(cheat_count)