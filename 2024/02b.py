reports = []
with open("./inputs/02.txt") as input:
    for line in input:
        report = line.split()
        report = [int(value) for value in report]
        reports.append(report)

def is_safe(report):
    rising, falling = True, True
    for val1, val2 in zip(report[1:], report[:-1]):
        if val1 > val2:
            rising = False
        if val1 < val2:
            falling = False
        if val1 == val2:
            return False
        if val1 - val2 > 3 or val2 - val1 > 3:
            return False
    if rising or falling:
        return True

safe_count = 0
for report in reports:
    safe = False
    for i in range(len(report)):
        if is_safe(report[:i] + report[i+1:]):
            safe = True
    if safe:
        safe_count += 1

print(safe_count)