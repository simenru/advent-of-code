from dataclasses import dataclass
import re

DIMX = 101
DIMY = 103

@dataclass
class Robot():
    x0: int
    y0: int
    vx: int
    vy: int

    def p_at(self, t: int) -> tuple[int, int]:
        x = self.x0 + t * self.vx
        y = self.y0 + t * self.vy

        x %= DIMX
        y %= DIMY

        return x, y

robots: list[Robot] = []
with open("inputs/14.txt") as input:
    for line in input:
        line = line.strip()
        m = re.match(r'p=(\d+),(\d+) v=(-?\d+),(-?\d+)', line)
        x0 = int(m.group(1))
        y0 = int(m.group(2))
        vx = int(m.group(3))
        vy = int(m.group(4))
        r = Robot(x0, y0, vx, vy)
        robots.append(r)

q1, q2, q3, q4 = 0, 0, 0, 0
for r in robots:
    x, y = r.p_at(100)
    if x < DIMX // 2:
        if y < DIMY // 2:
            q1 += 1
        elif y > DIMY // 2:
            q3 += 1
    elif x > DIMX // 2:
        if y < DIMY // 2:
            q2 += 1
        elif y > DIMY // 2:
            q4 += 1

print(q1 * q2 * q3 * q4)