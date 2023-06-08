from Grid import Grid
from A_Star import *
import sys
from heuristics import *

sys.setrecursionlimit(100000)

ITERATIONS = 100


def main(rows=10, start_pos=(0, 0), end_pos=(10, 10), maze=False, obstacles=[], visualize=False, heuristic=manhattan_h, time=False):

    grid = Grid(rows, rows, obstacles)
    grid.make_grid(rows)
    grid.make_obstacles()

    if maze:
        grid.generate_maze()

    start = grid.grid[start_pos[0]][start_pos[1]]
    goal = grid.grid[end_pos[0]][end_pos[1]]

    start.make_start()
    goal.make_end()

    for row in grid.grid:
        for cell in row:
            cell.update_neighbors(grid.grid)

    output = {}
    path, num = A_Star(grid.grid, start, goal, heuristic)

    output["map-size"] = rows
    output["nodes-expanded"] = num
    output["path-length"] = len(path)
    output["path-taken"] = path
    output["start"] = start_pos
    output["end"] = end_pos
    output["heuristic"] = heuristic
    if time:
        output["time"] = time_a_star(
            ITERATIONS, grid.grid, start, goal, heuristic)

    if visualize:
        grid.visualize(path)
    return output
