"""
test_cases.py

Example test grids.
Copy any grid, robot_initial, and max_moves to your main.py file to run them.
"""

# --- Test Case 1: 3x3 Grid Example ---

grid_3x3 = [
    [1, 3, 1],
    [0, 5, 0],
    [2, 0, 4]
]

robot_initial_3x3 = (2, 0)
max_moves_3x3 = 6

# Expected dirt: 15 (path example:  [(2, 0), (1, 0), (0, 0), (0, 1), (1, 1), (2, 1), (2, 2)])

# --- Test Case 2: Uneven Grid Example ---

grid_uneven = [
    [0, 3, 0],
    [2, 10, 1],
    [1, 0, 4]
]

robot_initial_uneven = (0, 0)
max_moves_uneven = 5

# Expected dirt: 18 (path example: [(0, 0), (0, 1), (1, 1), (2, 1), (2, 2), (1, 2)])

# --- Test Case 3: 5x5 Grid Example ---

grid_5x5 = [
    [2, 1, 3, 1, 2],
    [0, 4, 0, 5, 0],
    [3, 0, 6, 0, 1],
    [0, 7, 0, 4, 0],
    [5, 0, 2, 0, 3]
]

robot_initial_5x5 = (2, 2)
max_moves_5x5 = 10

# Expected dirt: 32 (path example: [(2, 2), (1, 2), (1, 3), (0, 3), (0, 2), (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (4, 0)])

"""
To use these test cases:
1. Copy the chosen grid, robot_initial, and max_moves into main.py.
2. Run: python main.py
3. Output should be similar to what is expected
"""
