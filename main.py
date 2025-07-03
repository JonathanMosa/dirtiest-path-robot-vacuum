# Define the grid of dirt values
grid = [
    [0, 3, 0],
    [2, 10, 1],
    [1, 0, 4]
]

# Starting position of the robot (row, col)
robot_initial = (0, 0)

# Number of allowed moves (battery limit)
max_moves = 5

# Get grid size
rows, cols = len(grid), len(grid[0])

# Define possible move directions: up, down, left, right
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# Visited cells set
visited = set()

# To store the best path found
best_path = []
# To store maximum dirt collected so far
max_dirt = [0]  # Use list so it can be updated inside function

# Recursive DFS function w/ path reconstruction
def dfs(r, c, moves_left, current_dirt, path):
    # If this cell was already visited, skip (can't collect dirt again)
    if (r, c) in visited:
        return

    # Mark current cell as visited
    visited.add((r, c))
    # Add this cell to current path
    path.append((r, c))

    # Update current collected dirt
    current_dirt += grid[r][c]

    # Check if this current path is better than the best so far
    if current_dirt > max_dirt[0]:
        max_dirt[0] = current_dirt
        # Save a copy of the current path as the best path
        best_path.clear()
        best_path.extend(path)

    # If no moves left, stop exploring further
    if moves_left == 0:
        # Backtrack: remove cell before returning
        visited.remove((r, c))
        path.pop()
        return

    # Explore all four directions
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols:
            dfs(nr, nc, moves_left - 1, current_dirt, path)

    # Backtrack: unmark cell and remove from path
    visited.remove((r, c))
    path.pop()

# Call DFS from initial position
dfs(robot_initial[0], robot_initial[1], max_moves, 0, [])

print("Maximum dirt collected:", max_dirt[0])
print("Best path to collect dirt:", best_path)
