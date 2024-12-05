import re

with open("./inputs/04.txt") as input:
    data = input.readlines()
    data = [line.strip() for line in data]

count = 0

# Horizontal
for l in data:
    count += len(re.findall(r'XMAS', l))
    count += len(re.findall(r'SAMX', l))

# Vertical
for l in map("".join, zip(*data)):
    count += len(re.findall(r'XMAS', l))
    count += len(re.findall(r'SAMX', l))

dimx = len(data[0])
dimy = len(data)

# Negative diagonal
## Starting top row
for l in ["".join([data[i][x0+i] for i in range(dimx - x0)]) for x0 in range(0, dimx)]:
    count += len(re.findall(r'XMAS', l))
    count += len(re.findall(r'SAMX', l))

## Starting left column
for l in ["".join([data[y0 + i][i] for i in range(dimy - y0)]) for y0 in range(1, dimy)]:
    count += len(re.findall(r'XMAS', l))
    count += len(re.findall(r'SAMX', l))


# Positive diagonal
## Starting left column
for l in ["".join([data[dimy - y0 - i - 1][i] for i in range(dimx - y0)]) for y0 in range(0, dimy)]:
    count += len(re.findall(r'XMAS', l))
    count += len(re.findall(r'SAMX', l))

## Starting bottom row
for l in ["".join([data[dimy - i - 1][x0 + i] for i in range(dimx - x0)]) for x0 in range(1, dimy)]:
    print(l)
    count += len(re.findall(r'XMAS', l))
    count += len(re.findall(r'SAMX', l))


print(count)