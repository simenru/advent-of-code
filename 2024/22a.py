import numpy as np

with open("inputs/22.txt") as f:
    monkeys = f.readlines()
    monkeys = [int(monkey.strip()) for monkey in monkeys]

monkeys = np.array(monkeys)

def mix_and_prune(m, n):
    return np.mod(np.bitwise_xor(m, n), 16777216)

def step(m):
    m = mix_and_prune(m, 64*m)
    m = mix_and_prune(m, np.floor_divide(m, 32))
    m = mix_and_prune(m, 2048*m)
    return m   

for _ in range(2000):
    monkeys = step(monkeys)

print(sum(monkeys)) #14180628689
