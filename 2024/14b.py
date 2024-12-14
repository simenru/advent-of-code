import re
import numpy as np

DIMX = 101
DIMY = 103

robots = np.zeros(shape=(0, 4), dtype=int)
with open("inputs/14.txt") as indata:
    for line in indata:
        line = line.strip()
        m = re.match(r'p=(\d+),(\d+) v=(-?\d+),(-?\d+)', line)
        x0 = int(m.group(1))
        y0 = int(m.group(2))
        vx = int(m.group(3))
        vy = int(m.group(4))
        robots = np.append(robots, [[x0, y0, vx, vy]], axis=0)

def step():
    robots[:, 0] += robots[:, 2]
    robots[:, 0] %= DIMX
    robots[:, 1] += robots[:, 3]
    robots[:, 1] %= DIMY

def draw_map():
    map = np.zeros(shape=(DIMX, DIMY))
    map[(robots[:,0], robots[:, 1])] = 1
    return map

def print_map(map):
    _, dimy = map.shape
    for y in range(dimy):
        line = "".join([" " if v == 0 else "X" for v in map[:,y]])
        print(line)

t = 0
while True:
    if t % 100 == 0:
        print(t)
    map = draw_map()

    for x,y in np.ndindex(map.shape):
        if x == 0 or y == 0 or x == DIMX-1 or y == DIMY-1:
            continue
        if np.sum(map[x-1:x+2,y-1:y+2]) == 9:
            print_map(map)
            input(f"{t=}")

    step()
    t += 1
