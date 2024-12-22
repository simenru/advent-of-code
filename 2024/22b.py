from collections import defaultdict
import numpy as np

with open("inputs/22.txt") as f:
    monkeys = f.readlines()
    monkeys = [int(monkey.strip()) for monkey in monkeys]

monkeys = np.array(monkeys)
monkeys = monkeys[:, np.newaxis]

def mix_and_prune(m, n):
    return np.mod(np.bitwise_xor(m, n), 16777216)

def step(m):
    m = mix_and_prune(m, 64*m)
    m = mix_and_prune(m, np.floor_divide(m, 32))
    m = mix_and_prune(m, 2048*m)
    return m   

#monkeys = np.array([1, 2, 3, 2024])[:, np.newaxis]

for _ in range(2000):
    monkeys = np.append(monkeys, step(monkeys[:, -1])[:, np.newaxis], axis=-1)

prices = np.mod(monkeys, 10)
diffs = prices[:, 1:] - prices[:, :-1]

change_values = defaultdict(lambda: np.full(shape=(len(monkeys)), fill_value=-1, dtype=int))
for t in range(2000-1-3):
    for m in range(len(monkeys)):
        change_val = tuple(diffs[m, t:t+4])
        if change_values[change_val][m] == -1:
            change_values[change_val][m] = prices[m, t+4]

totals = {k: sum(np.maximum(v, 0)) for k, v in change_values.items()}
print(totals[max(totals, key=totals.get)])