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
            # Nodes are:
            # A-----X1-B-C-X2-----D
            # With B, C not necessarily at integer coordinates

            dx = x2 - x1
            dy = y2 - y1
            # Node A:
            x = x1 - dx
            y = y1 - dy
            if 0<=x<dimx and 0<=y<dimy:
                nodes.add(f"({x},{y})")
            
            if dx % 3 == 0 and dy % 3 == 0:
                # Node B:
                x = x1 + dx/3
                y = y1 + dy/3
                nodes.add(f"({x},{y})")
                # Node C:
                x = x1 + dx/3
                y = y1 + dy/3
                nodes.add(f"({x},{y})")
            # Node D:
            x = x2 + dx
            y = y2 + dy
            if 0<=x<dimx and 0<=y<dimy:
                nodes.add(f"({x},{y})")

print(len(nodes))