from Cell import Cell
import random


class Grid:
    def __init__(self, width, height, obstacles=[]):
        self.width = width
        self.height = height
        self.grid = []
        self.obstacles = obstacles

    def make_obstacles(self):
        for each in self.obstacles:
            self.grid[each[0]][each[1]].make_barrier()

    def make_grid(self, rows):
        grid = []
        for i in range(rows):
            grid.append([])
            for j in range(rows):
                cell = Cell(i, j, rows)
                grid[i].append(cell)

        self.grid = grid

    def generate_maze(self):
        grid = [[0 for _ in range(self.width - 1)]
                for _ in range(self.width - 1)]

        def recursive_backtracking(x, y):
            grid[x][y] = 1
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            random.shuffle(directions)

            for dx, dy in directions:
                nx, ny = x + 2 * dx, y + 2 * dy
                if nx < 0 or ny < 0 or nx >= self.width - 1 or ny >= self.width - 1:
                    continue
                if grid[nx][ny] == 0:
                    grid[x + dx][y + dy] = 1
                    recursive_backtracking(nx, ny)

        recursive_backtracking(random.randrange(
            0, self.width - 1, 2), random.randrange(0, self.width - 1, 2))
        obstacles = []
        for i in range(0, self.width - 1):
            for j in range(0, self.width - 1):
                if grid[i][j] == 0:
                    obstacles.append((i, j))

        self.obstacles = obstacles
        self.make_obstacles()

    def visualize(self, path=[]):
        for y in range(self.height):
            row = []
            for x in range(self.width):
                if self.grid[x][y].is_start():
                    row.append("\033[1;34;43mS\033[0m")
                elif self.grid[x][y].is_end():
                    row.append("\033[1;33;44mE\033[0m")
                elif Cell(x, y, 0) in path:
                    row.append("\033[1;32mX\033[0m")
                elif self.grid[x][y].is_barrier():
                    row.append("\033[1;31m1\033[0m")
                elif self.grid[x][y].is_expanded():
                    row.append("\033[1;94mo\033[0m")
                else:
                    row.append('0')
            print(' '.join(row))
        print()
