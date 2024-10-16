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


def trace_back(path, search_space, heuristic=False, heuristic_func=heuristic1):
    # uniformed search:
    if heuristic == False:

        print("Representation of each Node:")
        print("(Depth, Cost, Operation, State)")
        cost = 0
        operation = "None"
        n = len(path)
        for i in range(n):
            print(f"({i}, {cost}, {operation},{path[i]})")

            if (i + 1 < n):
                ox, oy, od, = path[i]
                nx, ny, nd = path[i + 1]

                if (ox != nx or oy != ny):
                    operation = "Drill"
                    cost += search_space[nx][ny]
                elif ((od + 1) == nd):
                    operation = "Rotate Clockwise"
                    cost += 1
                elif ((od - 7) == nd):
                    operation = "Rotate Clockwise"
                    cost += 1
                elif ((od - 1) == nd):
                    operation = "Rotate Counter Clockwise"
                    cost += 1
                elif ((od + 7) == nd):
                    operation = "Rotate Counter Clockwise"
                    cost += 1
                else:
                    print("Traceback failed")
                    break

        print(f"Total Cost: {cost}")

    else:
        print("Representation of each Node:")
        print("(Depth, Cost, Operation, Heuristic, State)")
        cost = 0
        operation = "None"
        n = len(path)
        goal = path[-1]

        for i in range(n):

            pos = path[i]
            h = heuristic_func(pos, goal)
            print(f"({i}, {cost}, {operation},{h}, {h})")

            if (i + 1 < n):
                ox, oy, od, = path[i]
                nx, ny, nd = path[i + 1]

                if (ox != nx or oy != ny):
                    operation = "Drill"
                    cost += search_space[nx][ny]
                elif ((od + 1) == nd):
                    operation = "Rotate Clockwise"
                    cost += 1
                elif ((od - 7) == nd):
                    operation = "Rotate Clockwise"
                    cost += 1
                elif ((od - 1) == nd):
                    operation = "Rotate Counter Clockwise"
                    cost += 1
                elif ((od + 7) == nd):
                    operation = "Rotate Counter Clockwise"
                    cost += 1
                else:
                    print("Traceback failed")
                    break

        print(f"Total Cost: {cost}")
