from utils.get_neighbours import get_neighbours
from utils.traceback import trace_back

def dfs_recursive(current, target, cols, rows, parent):
    if (current[0] == target[0] and current[1] == target[1]):
        path = []
        while current:
            path.append(current)
            current = parent[current]
        path.reverse()
        # path.append(current)
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

    n = rows
    i = 1
    search_space = []

    while (n > 0):
        search_space.append(lines[i])
        i += 1
        n -= 1

    print("Search Space:")
    for line in search_space:
        print(line)

    start_position = tuple(lines[i])
    end_position = tuple(lines[i + 1])

    print("")
    print(f"start position: {start_position}")
    print(f"end position: {end_position}")
    print("")

    # We start searching bfs
    path = (dfs(start_position, end_position, cols, rows))
    trace_back(path, search_space)
    print(path)

