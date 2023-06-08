from main import main
from heuristics import *
import random
from memory_profiler import profile


# Config:
ROWS = 20
START = (10, 7)
END = (ROWS - 1, ROWS - 1)
MAZE = True
OBSTACLES = [(x, 10) for x in range(7, 14)] + [(10, y) for y in range(7, 14)]

VISUALIZE = False
TIME = True

# Table
TABLE = True
FIRST = "map-size"
SECOND = "time"

MIN_ROWS = 10
MAX_ROWS = 110
SKIP = 10

# Graph
GRAPH = False


def maze_builder(rows):
    grid = [[0 for _ in range(rows - 1)]
            for _ in range(rows - 1)]

    def recursive_backtracking(x, y):
        grid[x][y] = 1
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        random.shuffle(directions)

        for dx, dy in directions:
            nx, ny = x + 2 * dx, y + 2 * dy
            if nx < 0 or ny < 0 or nx >= rows - 1 or ny >= rows - 1:
                continue
            if grid[nx][ny] == 0:
                grid[x + dx][y + dy] = 1
                recursive_backtracking(nx, ny)

    recursive_backtracking(random.randrange(
        0, rows - 1, 2), random.randrange(0, rows - 1, 2))
    obstacles = []
    for i in range(0, rows - 1):
        for j in range(0, rows - 1):
            if grid[i][j] == 0:
                obstacles.append((i, j))

    return obstacles


# @profile(precision=4)
def build_table(file_name):
    with open(f"{file_name}.md", "w") as file:
        file.write(
            f"Grid Size | Manhattan Distance | Euclidian Distance | Diagnol Distance | Octile Distance |\n")
        file.write(f"| :-- | :-- | :-- | :-- | :-- |\n")
        for i in range(MIN_ROWS, MAX_ROWS):
            if i % SKIP == 0:
                start = (0, 0)
                manhattan = main(rows=i, start_pos=start, end_pos=(i - 1, i - 1), maze=MAZE,
                                 obstacles=OBSTACLES, visualize=VISUALIZE, heuristic=manhattan_h, time=TIME)
                euclidian = main(rows=i, start_pos=start, end_pos=(i - 1, i - 1), maze=MAZE,
                                 obstacles=OBSTACLES, visualize=VISUALIZE, heuristic=euclidian_h, time=TIME)
                octile = main(rows=i, start_pos=start, end_pos=(i - 1, i - 1), maze=MAZE,
                              obstacles=OBSTACLES, visualize=VISUALIZE, heuristic=octile_h, time=TIME)
                diagonal = main(rows=i, start_pos=start, end_pos=(i - 1, i - 1), maze=MAZE,
                                obstacles=OBSTACLES, visualize=VISUALIZE, heuristic=diagonal_h, time=TIME)
                file.write(
                    f"{manhattan[FIRST]} | {manhattan[SECOND]:.3f} | {euclidian[SECOND]:.3f} | {octile[SECOND]:.3f} | {diagonal[SECOND]:.3f} |\n")


if __name__ == "__main__":
    build_table(
        f"{FIRST}-vs-{SECOND}-maze")
