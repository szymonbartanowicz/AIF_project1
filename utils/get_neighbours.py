def get_neighbours(position, cols, rows):
    x, y, d = position

    xx = x
    yy = y

    neighbours = []

    # Drill in direction currently facing:
    if d == 0:
        x -= 1
    elif d == 1:
        x -= 1
        y += 1
    elif d == 2:
        y += 1
    elif d == 3:
        x += 1
        y += 1
    elif d == 4:
        x += 1
    elif d == 5:
        x += 1
        y -= 1
    elif d == 6:
        y -= 1
    elif d == 7:
        y -= 1
        x -= 1

    if ((x >= 0 and x < rows) and (y >= 0 and y < cols)):
        neighbours.append((x, y, d))

    # Turn:
    rd = (d - 1) % 8
    ld = (d + 1) % 8

    neighbours.append((xx, yy, rd))
    neighbours.append((xx, yy, ld))

    return (neighbours)