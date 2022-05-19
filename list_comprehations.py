x = int(input())
y = int(input())
z = int(input())
n = int(input())

coords = []
for x in range(x + 1):
    for y in range(y + 1):
        for z in range(z + 1):
            coords.append([x, y, z])
coords = [cords for cords in coords if not sum(cords) == n]

print(coords)
