import random
import queue
import heapq

RED = "\033[91m"
BLUE = "\033[94m"
GREEN = "\033[92m"
ENDC = "\033[0m"

def generate_maze(n):
    maze = [[BLUE + '◌' + ENDC for _ in range(n)] for _ in range(n)]

    # Place start (S) and end (E)
    maze[0][0] = 'S'
    maze[n-1][n-1] = 'E'

    # Place random walls
    num_walls = int(0.22 * n * n)
    for _ in range(num_walls):
        row, col = random.randint(0, n-1), random.randint(0, n-1)
        maze[row][col] = RED + '▓' + ENDC  # Walls

    return maze

def print_colored_maze(maze):
    for row in maze:
        print(" ".join(row))
    print()

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star(maze, start, end):
    q = []
    heapq.heappush(q, (0, start))
    visited = set()
    parent = {}

    while q:
        current_cost, current = heapq.heappop(q)

        if current == end:
            path = []
            while current in parent:
                path.insert(0, current)
                current = parent[current]
            path.insert(0, start)
            return path
        
        if current in visited:
            continue

        visited.add(current)

        for neighbor in neighbors(current, maze):
            if neighbor not in visited:
                cost = current_cost + 1 + heuristic(neighbor, end)
                heapq.heappush(q, (cost, neighbor))
                parent[neighbor] = current

    return None

def neighbors(cell, maze):
    row, col = cell
    n = len(maze)
    m = len(maze[0])

    potential_neighbors = [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]
    valid_neighbors = [(r, c) for r, c in potential_neighbors if 0 <= r < n and 0 <= c < m and maze[r][c] != RED + '▓' + ENDC]

    return valid_neighbors

def print_colored_path(maze, path):
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            if (row, col) == tuple(path[0]):
                maze[row][col] = GREEN + 'S' + ENDC
            elif (row, col) == tuple(path[-1]):
                maze[row][col] = GREEN + 'E' + ENDC
            elif (row, col) in path:
                maze[row][col] = GREEN + '◍' + ENDC  # Path
            elif maze[row][col] == BLUE + '◌' + ENDC:
                maze[row][col] = BLUE + '◌' + ENDC  # Open space
            elif maze[row][col] == RED + '▓' + ENDC:
                maze[row][col] = RED + '▓' + ENDC  # Walls

    print_colored_maze(maze)

def mark_colored_path(maze, path):
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            if (row, col) == tuple(path[0]):
                maze[row][col] = GREEN + 'S' + ENDC
            elif (row, col) == tuple(path[-1]):
                maze[row][col] = GREEN + 'E' + ENDC
            elif (row, col) in path:
                maze[row][col] = GREEN + '◍' + ENDC  # Path
            elif maze[row][col] == BLUE + '◌' + ENDC:
                maze[row][col] = BLUE + '◌' + ENDC  # Open space
            elif maze[row][col] == RED + '▓' + ENDC:
                maze[row][col] = RED + '▓' + ENDC  # Walls

    return maze

def main():
    while True:
        n = int(input("Enter the size of the maze (n * n): "))
        maze = generate_maze(n)

        print("Generated Maze:")
        print_colored_maze(maze)

        option = int(input("Choose an option:(1: Print Path, 2: Generate Another Puzzle, 3: Exit): "))

        