point1 = (3, 5)
print("Point 1:", point1)

point2 = (7, 2)
print("Point 2:", point2)

x1, y1 = point1
print("x1 =", x1, "y1 =", y1)

x2, y2 = point2
print("x2 =", x2, "y2 =", y2)

distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print("Distance between points:", distance)

chars = tuple("PYTHON")
print("Characters tuple:", chars)

for c in chars:
    print(c)
