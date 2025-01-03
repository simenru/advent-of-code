import rasterio
import numpy as np
import rasterio.features
import shapely

with open("inputs/12.txt") as input:
    data = []
    for line in input:
        data.append(line.strip())

dimx, dimy = len(data[0]), len(data)

map = np.zeros(shape=(dimx, dimy))

value_map = {}
num_values = 0
for y in range(dimy):
    for x in range(dimx):
        value = data[y][x]
        if value in value_map:
            map[y][x] = value_map[value]
        else:
            value_map[value] = num_values + 1
            num_values += 1
            map[y][x] = value_map[value]

def get_num_perimeter_sections(polygon: shapely.Polygon) -> int:
    perimeter = 0
    perimeter += len(polygon.exterior.coords) - 1
    for linearring in polygon.interiors:
        perimeter += len(linearring.coords) - 1
    return perimeter

price = 0
for geojson, _ in rasterio.features.shapes(map):
    shape = shapely.geometry.shape(geojson)

    area = shape.area
    perimeter = 0
    if isinstance(shape, shapely.Polygon):
        perimeter += get_num_perimeter_sections(shape)
    elif isinstance(shape, shapely.MultiPolygon):
        for p in shape.geoms:
            perimeter += get_num_perimeter_sections(p)
    
    price += area * perimeter

print(price)