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
        current_cost, current = heapqfs