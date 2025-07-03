# dirtiest-path-robot-vacuum

This project implements a specialized pathfinding algorithm for a robot vacuum to maximize dirt collection within a limited number of moves (battery constraint). The algorithm adapts classic Depth-First Search (DFS) into a new real-world use case by tracking visited cells and reconstructing the exact optimal path. Unlike simple greedy approaches, this method guarantees maximum total dirt.

---

## Files included

* `main.py`: Main implementation of the DFS-based dirt collection algorithm.
* `test_cases.py`: Example test cases matching the grids shown in the presentation slides.
* `README.md`: This documentation file with instructions and project overview.

---

## How to run

- cd into file where main.py is located
- run in the terminal python main.py

### Editing to try different test scenarios

To try different grids, edit these within the main.py: 
- grid: The layout of the dirt values
- robot_initial: Starting position of the robot as a tuple (row, column)
- max_moves: Maximum number of moves (battery limit)

The program will output:
- Maximum dirt collected
- Best path taken to get the maximum dirt
