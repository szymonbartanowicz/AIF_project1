from utils.get_neighbours import get_neighbours
from utils.traceback import trace_back


def heuristic1(start, target):
    y1, x1, o1 = start
    y2, x2, o2 = target

    diffx = x2 - x1
    diffy = y2 - y1

    dist = max(abs(diffx), abs(diffy))

    if diffx == 0:
        if diffy > 0:
            dir_id = 4
        elif diffy <= 0:
            dir_id = 0
    elif diffy == 0:
        if diffx > 0:
            dir_id = 2
        elif diffx <= 0:
            dir_id = 6
    else:
        if diffx > 0 and diffy > 0:
            dir_id = 3
        elif diffx < 0 and diffy > 0:
            dir_id = 5
        elif diffx < 0 and diffy < 0:
            dir_id = 7
        elif diffx > 0 and diffy < 0:
            dir_id = 1

    turns = min(abs(dir_id - o1), 8 - abs(o1 - dir_id))
    return (turns + dist)


def aStar_1(start, target, cols, rows, search_space):
    # Check if we start and target, then there is nothing to do
    if start[0] == target[0] and start[1] == target[1]:
        return ([start])

    queue = [(start, 0)]

    # dictionary to trace back (save parent node)
    parent = {start: None}

    # Initialize the cost from start to a node (g)
    g_score = {}
    g_score[start] = 0

    # Initialize the estimated total cost (f = g + h)
    f_score = {}
    f_score[start] = heuristic1(start, target)

    while queue:

        print(f"queue: {queue}")
        current_tup = min(queue, key=lambda t: t[1])
        queue.remove(current_tup)

        current = current_tup[0]
        print(f"current {current}")

        # check if current is target
        if current[0] == target[0] and current[1] == target[1]:
            path = []
            while current:
                path.append(current)
                current = parent[current]
            path.reverse()
            # path.append(neighbour)
            print(f"Path found from goal to target with A_Start Search: {path}")
            return path

        for neighbour in get_neighbours(current, cols, rows):
            # only use neigbhours that are not yet visited
            if neighbour not in parent:

                print(f"Current neighbour: {neighbour}")
                # Calculate tentative g_score (current cost to reach this neighbor)
                current_g = g_score[current] + distance(current, neighbour, search_space)

                if neighbour not in queue or (current_g < g_score.get(neighbour, float('inf'))):
                    # Record the best path so far
                    parent[neighbour] = current
                    g_score[neighbour] = current_g
                    f_score[neighbour] = current_g + heuristic1(neighbour, target)

                    if neighbour not in queue:
                        queue.append((neighbour, f_score[neighbour]))


def distance(current, neighbour, search_space):
    if current[2] != neighbour[2]:
        return 1
    else:
        # print(search_space[neighbour[0]][neighbour[1]])
        return search_space[neighbour[0]][neighbour[1]]


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

    path = (aStar_1(start_position, end_position, cols, rows, search_space))
    print(path)
    trace_back(path, search_space, True, heuristic1)



