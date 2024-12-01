list1, list2 = [], []

with open("./inputs/01.txt") as input:
    for line in input:
        item1, item2 = line.split()
        list1.append(int(item1))
        list2.append(int(item2))

counts = {}
for item in list2:
    if item in counts:
        counts[item] += 1
    else:
         counts[item] = 1

similarity = 0
for item in list1:
    if item in counts:
        similarity += item * counts[item]

print(similarity)