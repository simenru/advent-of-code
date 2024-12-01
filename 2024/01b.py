from collections import Counter

list1, list2 = [], []

with open("./inputs/01.txt") as input:
    for line in input:
        item1, item2 = line.split()
        list1.append(int(item1))
        list2.append(int(item2))

counts = Counter(list2)

similarity = 0
for item in list1:
    similarity += item * counts[item]

print(similarity)