from dataclasses import dataclass
import re


@dataclass
class Machine():
    button_a: tuple[int, int]
    button_b: tuple[int, int]
    prize: tuple[int, int]

machines = []

with open("inputs/13.txt") as input:
    lines = input.readlines()

    for i in range(len(lines) // 4 + 1):
        ma = re.match(r'Button A: X\+(\d+), Y\+(\d+)', lines[4*i])
        mb = re.match(r'Button B: X\+(\d+), Y\+(\d+)', lines[4*i+1])
        mp = re.match(r'Prize: X=(\d+), Y=(\d+)', lines[4*i+2])
        if ma is None:
            print(i)
        m = Machine(
            button_a=(int(ma.group(1)), int(ma.group(2))),
            button_b=(int(mb.group(1)), int(mb.group(2))),
            prize=(int(mp.group(1)), int(mp.group(2)))
        )
        machines.append(m)

def solve_machine(m: Machine) -> tuple[int, int] | None:
    a, d = m.button_a
    b, e = m.button_b
    c, f = m.prize

    det = a*e - b*d

    press_b = (a*f - c*d) / det
    press_a = c/a - b*press_b / a

    

    ipress_a, ipress_b = round(press_a), round(press_b)
    
    if a*ipress_a + b*ipress_b != c or d*ipress_a + e*ipress_b != f or ipress_a < 0 or ipress_a > 100 or ipress_b < 0 or ipress_b > 100:
        print(m, press_a, press_b)
        print(a*ipress_a + b*ipress_b, c, d*ipress_a + e*ipress_b, f)
        print("Failed!")
        return None

    return ipress_a, ipress_b

cost = 0
for m in machines:
    solution = solve_machine(m)
    if solution is None:
        continue
    a, b = solution
    cost += 3*a + b

#print(solve_machine(Machine((94, 34), (22, 67), (8400, 5400))))

print(cost)