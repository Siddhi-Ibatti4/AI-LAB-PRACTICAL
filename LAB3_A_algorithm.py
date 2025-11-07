import math
from heapq import heappush, heappop

# Heuristic functions
def manhattan(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def euclidean(a, b):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

# A* search
def astar(start, goal, grid, heuristic=manhattan):
    rows, cols = len(grid), len(grid[0])
    open_list = [(0, start, [start])]  # (f, node, path)
    visited = set()

    while open_list:
        f, current, path = heappop(open_list)
        if current == goal:
            return path
        if current in visited:
            continue
        visited.add(current)

        x, y = current
        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:  # 4 directions
            nx, ny = x+dx, y+dy
            if 0<=nx<rows and 0<=ny<cols and grid[nx][ny]==0:
                g = len(path)
                h = heuristic((nx, ny), goal)
                heappush(open_list, (g+h, (nx, ny), path+[(nx, ny)]))
    return None

# Example grid (0=free, 1=blocked)
grid = [
    [0,0,0,0,1],
    [1,1,0,1,0],
    [0,0,0,0,0],
    [0,1,1,1,0],
    [0,0,0,0,0]
]

start, goal = (0,0), (4,4)

print("Manhattan Path:", astar(start, goal, grid, manhattan))
print("Euclidean Path:", astar(start, goal, grid, euclidean))

