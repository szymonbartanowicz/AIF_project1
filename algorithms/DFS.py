import sys


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

    if ((x >= 0 and x < cols) and (y >= 0 and y < rows)):
        neighbours.append((x, y, d))

    # Turn:
    rd = (d - 1) % 8
    ld = (d + 1) % 8

    neighbours.append((xx, yy, rd))
    neighbours.append((xx, yy, ld))

    return (neighbours)


def bfs(start, target, cols, rows):
    # Check if we start and target, then there is nothing to do
    if start[0] == target[0] and start[1] == target[1]:
        return ([start])

    # fifo queue to expand frontier
    queue = [start]

    # dictionary to trace back (save parent node)
    parent = {start: None}

    while queue:
        current = queue.pop(0)

        # find the neigbhours of current node
        for neighbour in get_neighbours(current, cols, rows):
            # only use neigbhours that are not yet visited
            if neighbour not in parent:
                # check if neigbhour is the target
                if not (neighbour[0] == target[0] and neighbour[1] == target[1]):
                    # if not append to queue and set current node as its parent
                    queue.append(neighbour)
                    parent[neighbour] = current
                else:
                    # if yes we found a solution and trace back to print the path
                    path = []
                    while current:
                        path.append(current)
                        current = parent[current]
                    path.reverse()
                    path.append(neighbour)
                    print(f"Path found from goal to target with BFS Search: {path}")
                    return path
        print(f"current queue: {queue}")
    return False


def dfs_recursive(current, target, cols, rows, parent):
    if (current[0] == target[0] and current[1] == target[1]):
        path = []
        while current:
            path.append(current)
            current = parent[current]
        path.reverse()
        path.append(current)
        print(parent)
        # print(f"Path found from goal to target with DFS Search: {path}")
        return path
    else:
        for neighbour in get_neighbours(current, cols, rows):
            # only use neigbhours that are not yet visited
            # print(f"Current Neigbhour: {neighbour}")
            if neighbour not in parent:
                # print(f"New Node Explored: {neighbour}")
                parent[neighbour] = current
                result = dfs_recursive(neighbour, target, cols, rows, parent)
                if result:
                    return result

    return None


def dfs(start, target, cols, rows):
    # Check if we start at target, then there is nothing to do
    if start[0] == target[0] and start[1] == target[1]:
        return ([start])

    # dictionary to trace back (save parent node), check if node is explored
    parent = {start: None}

    # recursively check search space
    return dfs_recursive(start, target, cols, rows, parent)


def main(input_file):
    with open(input_file, 'r') as file:
        lines = file.read()

    lines = lines.split("\n")

    new_lines = []
    for line in lines:
        new_line = line.split()
        for i in range(len(new_line)):
            new_line[i] = int(new_line[i])
        new_lines.append(new_line)

    lines = new_lines

    in1 = lines[0]

    rows = int(in1[0])
    cols = int(in1[1])

    n = cols
    i = 1
    search_space = []

    while (n > 1):
        search_space.append(lines[i])
        i += 1
        n -= 1

    print("Search Space:")
    for line in search_space:
        print(line)

    print(lines)
    start_position = tuple(lines[i])
    end_position = tuple(lines[i + 1])

    print("")
    print(f"start position: {start_position}")
    print(f"end position: {end_position}")
    print("")

    # We start searching bfs
    # bfs(start_position, end_position, cols, rows)

    dfs(start_position, end_position, cols, rows)



