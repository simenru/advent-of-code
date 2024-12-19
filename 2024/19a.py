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
def possible_pattern(pattern: str) -> bool:
    if pattern == "":
        return True

    for towel in towels:
        if pattern.startswith(towel):
            if possible_pattern(pattern[len(towel):]):
                return True

    return False

count = 0
for pattern in patterns:
    if possible_pattern(pattern):
        count += 1
    
print(count)