list1, list2 = [], []

with open("./inputs/01.txt") as input:
    for line in input:
        item1, item2 = line.split()
        list1.append(int(item1))
        list2.append(int(item2))

list1 = sorted(list1)
list2 = sorted(list2)

distance = 0
for item1, item2 in zip(list1, list2):
    distance += abs(item1 - item2)

print(distance)