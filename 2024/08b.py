from math import gcd

signal_map = []
with open("inputs/08.txt") as input:
    for line in input:

        line = line.strip()
        signal_map.append(line)

dimx, dimy = len(signal_map[0]), len(signal_map)

coordinate_map = {}
for y, line in enumerate(signal_map):
    for x, c in enumerate(line):
        if c == ".":
            continue
        if c in coordinate_map:
            coordinate_map[c].append((x, y))
        else:
            coordinate_map[c] = [(x, y)]

nodes = set()
for _, coordinate_list in coordinate_map.items():
    for x1, y1 in coordinate_list:
        for x2, y2 in coordinate_list:
            if x1 == x2 and y1 == y2:
                continue

            dx = x2 - x1
            dy = y2 - y1
            
            g = gcd(dx, dy)
            dx, dy = dx//g, dy//g

            x, y  = x1, y1
            while 0<=x<dimx and 0<=y<dimy:
                nodes.add(f"({x},{y})")
                x, y = x-dx, y-dy
            
            x, y  = x1, y1
            while 0<=x<dimx and 0<=y<dimy:
                nodes.add(f"({x},{y})")
                x, y = x+dx, y+dy
            
#print(nodes)

print(len(nodes))