from functools import cache

patterns = []

with open("inputs/19.txt") as f:
    towels = f.readline()
    towels = towels.strip()
    towels = towels.split(", ")

    f.readline()

    for pattern in f:
        pattern = pattern.strip()
        patterns.append(pattern)

@cache
def possible_pattern(pattern: str) -> int:
    if pattern == "":
        return 1

    possible = 0
    for towel in towels:
        if pattern.startswith(towel):
            possible += possible_pattern(pattern[len(towel):])
    
    return possible

count = 0
for pattern in patterns:
    count += possible_pattern(pattern)
    
print(count)