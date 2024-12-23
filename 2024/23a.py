from collections import defaultdict

connections = defaultdict(set)

with open("inputs/23.txt") as f:
    for line in f:
        line = line.strip()
        a, b = line.split("-")
        connections[a].add(b)
        connections[b].add(a)

cycles = set()

for c1 in connections:
    for c2 in connections[c1]:
        for c3 in connections[c1].intersection(connections[c2]):
            if c1 != c2 and c1 != c3 and c2 != c3:
                cycles.add(tuple(sorted([c1, c2, c3])))

count = 0
for c1, c2, c3 in cycles:
    if c1.startswith("t") or c2.startswith("t") or c3.startswith("t"):
        count += 1
print(count)