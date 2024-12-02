reports = []
with open("./inputs/02.txt") as input:
    for line in input:
        report = line.split()
        report = [int(value) for value in report]
        reports.append(report)

safe_count = 0
for report in reports:
    rising, falling, safe = True, True, True
    for val1, val2 in zip(report[1:], report[:-1]):
        if val1 > val2:
            rising = False
        if val1 < val2:
            falling = False
        if val1 == val2:
            safe = False
        if val1 - val2 > 3 or val2 - val1 > 3:
            safe = False
    
    if (rising or falling) and safe:
        safe_count += 1

print(safe_count)