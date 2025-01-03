with open("inputs/12.txt") as input:
    data = []
    for line in input:
        data.append(line.strip())

dimx, dimy = len(data[0]), len(data)

visited = set()

def calculate_area_and_perimeter(x, y):
    visited.add(f"{x},{y}")
    area = 1
    perimeter = 0

    if x-1 >= 0 and data[y][x-1] == data[y][x]:
        if f"{x-1},{y}" not in visited:
            delta_a, delta_p = calculate_area_and_perimeter(x-1, y)
            area += delta_a
            perimeter += delta_p
    else:
        perimeter += 1

    if x+1 < dimx and data[y][x+1] == data[y][x]:
        if f"{x+1},{y}" not in visited:
            delta_a, delta_p = calculate_area_and_perimeter(x+1, y)
            area += delta_a
            perimeter += delta_p
    else:
        perimeter += 1

    if y-1 >= 0 and data[y-1][x] == data[y][x]:
        if f"{x},{y-1}" not in visited:
            delta_a, delta_p = calculate_area_and_perimeter(x, y-1)
            area += delta_a
            perimeter += delta_p
    else:
        perimeter += 1

    if y+1 < dimy and data[y+1][x] == data[y][x]:
        if f"{x},{y+1}" not in visited:
            delta_a, delta_p = calculate_area_and_perimeter(x, y+1)
            area += delta_a
            perimeter += delta_p
    else:
        perimeter += 1

    return area, perimeter


price = 0
for y in range(dimy):
    for x in range(dimx):
        if f"{x},{y}" in visited:
            continue

        area, perimeter = calculate_area_and_perimeter(x, y)
        price += area * perimeter

print(price)
        