from collections import defaultdict

with open("inputs/11.txt") as input:
    stones = input.readline()
    stones = stones.strip()
    stones = stones.split()
    stones = [int(s) for s in stones]

counts = defaultdict(int)
for stone in stones:
    counts[stone] = 1

def step(counts):
    new_counts = defaultdict(int)
    for stone, count in counts.items():
        if stone == 0:
            new_counts[1] += count
        elif len(str(stone)) % 2 == 0:
            stone = str(stone)
            s1 = int(stone[:len(stone)//2])
            s2 = int(stone[len(stone)//2:])
            new_counts[s1] += count
            new_counts[s2] += count
        else:
            new_counts[2024*stone] += count
    return new_counts

for i in range(75):
    counts = step(counts)
