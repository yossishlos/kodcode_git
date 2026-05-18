def distance_between_points(point1: tuple, point2: tuple):
    x1, y1 = point1
    x2, y2 = point2
    result = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5
    return result
print(distance_between_points((0, 0), (3, 4)))