patterns = []

with open("inputs/19.txt") as f:
    towels = f.readline()
    towels = towels.strip()
    towels = towels.split(", ")

    f.readline()

    for pattern in f:
        pattern = pattern.strip()
        patterns.append(pattern)

possible_patterns: dict[str, bool] = {}

for towel in towels:
    possible_patterns[towel] = True

def possible_pattern(pattern: str) -> bool:
    if pattern in possible_patterns:
        return possible_patterns[pattern]

    possible = False
    for towel in towels:
        if pattern.startswith(towel):
            if possible_pattern(pattern[len(towel):]):
                possible = True
    
    possible_patterns[pattern] = possible
    return possible

count = 0
for pattern in patterns:
    print(pattern)
    if possible_pattern(pattern):
        count += 1
    
print(count)