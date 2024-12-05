import re

with open("./inputs/04.txt") as input:
    data = input.readlines()
    data = [line.strip() for line in data]

count = 0

dimx = len(data[0])
dimy = len(data)

for x in range(1, dimx - 1):
    for y in range(1, dimy - 1):
        if data[y][x] != "A":
            continue
        # M.S
        # .A.
        # M.S
        if data[y-1][x-1] == "M" and data[y-1][x+1] == "S" and data[y+1][x-1] == "M" and data[y+1][x+1] == "S":
            count += 1
        # M.M
        # .A.
        # S.S
        elif data[y-1][x-1] == "M" and data[y-1][x+1] == "M" and data[y+1][x-1] == "S" and data[y+1][x+1] == "S":
            count += 1
        #
        # S.M
        # .A.
        # S.M
        elif data[y-1][x-1] == "S" and data[y-1][x+1] == "M" and data[y+1][x-1] == "S" and data[y+1][x+1] == "M":
            count += 1
        #
        # S.S
        # .A.
        # M.M
        elif data[y-1][x-1] == "S" and data[y-1][x+1] == "S" and data[y+1][x-1] == "M" and data[y+1][x+1] == "M":
            count += 1

print(count)