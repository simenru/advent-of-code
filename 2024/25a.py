import numpy as np

with open("inputs/25.txt") as f:
    lines = f.readlines()

patterns = []
current_pattern = []
for line in lines:
    line = line.strip()
    if line == "":
        patterns.append(current_pattern)
        current_pattern = []
    else:
        current_pattern.append(line)
patterns.append(current_pattern)

patterns = [[[0 if c == "." else 1 for c in line] for line in pattern] for pattern in patterns]

patterns = [np.array(pattern) for pattern in patterns]

keys = [p for p in patterns if sum(p[-1,:]) == 5]
keys = [p.sum(axis=0) for p in keys]
locks = [p for p in patterns if sum(p[0,:]) == 5]
locks = [p.sum(axis=0) for p in locks]

count = 0
for key in keys:
    for lock in locks:
        s = key + lock
        if max(s) <= 7:
            count += 1
            
print(count)