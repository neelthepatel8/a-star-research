from Grid import Grid
from Cell import Cell
from astar import astar
from heuristics import *


def main():
    grid = Grid(10, 10)

    grid.set_cell(Cell(3, 3), 1)
    grid.set_cell(Cell(3, 4), 1)
    grid.set_cell(Cell(4, 3), 1)
    grid.set_cell(Cell(4, 4), 1)

    start = Cell(1, 1)
    end = Cell(8, 8)

    euclidian_path = astar(grid, start, end, manhattan_distance)
    # manhattan_path = astar(grid, start, end, manhattan_distance)

    grid.visualize_path(start, end, euclidian_path)
    # grid.visualize_path(start, end, manhattan_path)


if __name__ == "__main__":
    main()
