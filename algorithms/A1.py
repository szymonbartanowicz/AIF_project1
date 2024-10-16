import heapq
import math

# Directions: North, Northeast, East, Southeast, South, Southwest, West, Northwest
DIRECTIONS = [
    (-1, 0),  # North
    (-1, 1),  # Northeast
    (0, 1),  # East
    (1, 1),  # Southeast
    (1, 0),  # South
    (1, -1),  # Southwest
    (0, -1),  # West
    (-1, -1)  # Northwest
]


# A* Algorithm
def astar(grid, start, goal):
    n, m = len(grid), len(grid[0])
    (x_start, y_start, orientation_start) = start
    (x_goal, y_goal, orientation_goal) = goal

    # Priority queue (min-heap) for A* frontier
    frontier = []
    heapq.heappush(frontier, (0, x_start, y_start, orientation_start))

    # Maps to store the cost to reach each node and its previous node for path reconstruction
    cost_so_far = {}
    cost_so_far[(x_start, y_start, orientation_start)] = 0

    came_from = {}
    came_from[(x_start, y_start, orientation_start)] = None

    while frontier:
        _, x, y, orientation = heapq.heappop(frontier)

        # Check if we've reached the goal (ignoring orientation if it's irrelevant)
        if (x, y) == (x_goal, y_goal) and (orientation == orientation_goal or orientation_goal == 8):
            return reconstruct_path(came_from, start, (x, y, orientation))

        # Explore neighbors
        for i, (dx, dy) in enumerate(DIRECTIONS):
            new_x, new_y = x + dx, y + dy
            new_orientation = i

            if 0 <= new_x < n and 0 <= new_y < m:  # Check boundaries
                new_cost = cost_so_far[(x, y, orientation)] + grid[new_x][new_y]

                # Consider new state only if it's better (lower cost)
                if (new_x, new_y, new_orientation) not in cost_so_far or new_cost < cost_so_far[
                    (new_x, new_y, new_orientation)]:
                    cost_so_far[(new_x, new_y, new_orientation)] = new_cost

                    # Priority: f = g (cost so far) + h (heuristic)
                    priority = new_cost + heuristic(new_x, new_y, x_goal, y_goal)
                    heapq.heappush(frontier, (priority, new_x, new_y, new_orientation))

                    # Track the path
                    came_from[(new_x, new_y, new_orientation)] = (x, y, orientation)

    # No path found
    return None


# Euclidean distance heuristic
def heuristic(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


# Reconstruct the path from start to goal
def reconstruct_path(came_from, start, goal):
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = came_from[current]
    path.reverse()
    return path


# Main function to run the program
def main(input_file):
    with open(input_file, 'r') as file:
        input_data = file.read()

    # Parsing input
    lines = input_data.strip().split("\n")

    # Grid size
    n, m = map(int, lines[0].split())

    # Grid map
    grid = [list(map(int, lines[i + 1].split())) for i in range(n)]

    # Initial position (x, y, orientation)
    x_start, y_start, orientation_start = map(int, lines[n + 1].split())

    # Target position (x, y, orientation)
    x_goal, y_goal, orientation_goal = map(int, lines[n + 2].split())

    start = (x_start, y_start, orientation_start)
    goal = (x_goal, y_goal, orientation_goal)

    # Run A* algorithm
    path = astar(grid, start, goal)

    # Output the result
    if path:
        print("Path found:", path)
    else:
        print("No path found")

