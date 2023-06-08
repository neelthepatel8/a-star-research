import pygame
from queue import PriorityQueue
from Color import *
from heuristics import *

WIDTH = 800
SCREEN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("A* Path Finding Algorithm")


class Cell:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = WHITE
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows

    def get_pos(self):
        return self.row, self.col

    def is_closed(self):
        return self.color == CLOSED

    def is_open(self):
        return self.color == OPEN

    def is_barrier(self):
        return self.color == OBSTACLE

    def is_start(self):
        return self.color == START

    def is_end(self):
        return self.color == END

    def reset(self):
        self.color = WHITE

    def make_start(self):
        self.color = START

    def make_closed(self):
        self.color = CLOSED

    def make_open(self):
        self.color = OPEN

    def make_barrier(self):
        self.color = OBSTACLE

    def make_end(self):
        self.color = END

    def make_path(self):
        self.color = PATH

    def draw(self, screen):
        pygame.draw.rect(
            screen, self.color, (self.x, self.y, self.width, self.width))

    def update_neighbors(self, grid):
        self.neighbors = []
        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_barrier():
            self.neighbors.append(grid[self.row + 1][self.col])

        if self.row > 0 and not grid[self.row - 1][self.col].is_barrier():
            self.neighbors.append(grid[self.row - 1][self.col])

        if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_barrier():
            self.neighbors.append(grid[self.row][self.col + 1])

        if self.col > 0 and not grid[self.row][self.col - 1].is_barrier():
            self.neighbors.append(grid[self.row][self.col - 1])

    def __lt__(self, other):
        return False


def make_path_out_of_both(came_from, current, draw):
    while current in came_from:
        current = came_from[current]
        current.make_path()
        draw()


def a_star(draw, grid, start, end, heuristic):
    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, start))
    came_from = {}
    g_score = {cell: float("inf") for row in grid for cell in row}
    g_score[start] = 0
    f_score = {cell: float("inf") for row in grid for cell in row}
    f_score[start] = heuristic(start, end)

    open_set_hash = {start}

    while not open_set.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = open_set.get()[2]
        open_set_hash.remove(current)

        if current == end:
            make_path_out_of_both(came_from, end, draw)
            end.make_end()
            return True

        for neighbor in current.neighbors:
            temp_g_score = g_score[current] + 1

            if temp_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = temp_g_score + \
                    heuristic(neighbor, end)
                if neighbor not in open_set_hash:
                    count += 1
                    open_set.put((f_score[neighbor], count, neighbor))
                    open_set_hash.add(neighbor)
                    neighbor.make_open()

        draw()

        if current != start:
            current.make_closed()

    return False


def make_grid(rows, width):
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            cell = Cell(i, j, gap, rows)
            grid[i].append(cell)

    return grid


def draw_grid(screen, rows, width):
    gap = width // rows
    for row in range(rows):
        pygame.draw.line(screen, GREY, (0, row * gap), (width, row * gap))
        for col in range(rows):
            pygame.draw.line(screen, GREY, (col * gap, 0), (col * gap, width))


def draw(screen, grid, rows, width):
    screen.fill(WHITE)

    for row in grid:
        for cell in row:
            cell.draw(screen)

    draw_grid(screen, rows, width)
    pygame.display.update()


def get_clicked_pos(pos, rows, width):
    gap = width // rows
    y, x = pos

    row = y // gap
    col = x // gap

    return row, col


def main(screen, width):
    ROWS = 40
    grid = make_grid(ROWS, width)

    start = None
    end = None

    run = True
    while run:
        draw(screen, grid, ROWS, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                cell = grid[row][col]
                if not start and cell != end:
                    start = cell
                    start.make_start()

                elif not end and cell != start:
                    end = cell
                    end.make_end()

                elif cell != end and cell != start:
                    cell.make_barrier()

            elif pygame.mouse.get_pressed()[2]:
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                cell = grid[row][col]
                cell.reset()
                if cell == start:
                    start = None
                elif cell == end:
                    end = None

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1 and start and end:
                    for row in grid:
                        for cell in row:
                            cell.update_neighbors(grid)

                    a_star(lambda: draw(screen, grid, ROWS, width),
                           grid, start, end, manhattan_distance)

                elif event.key == pygame.K_2 and start and end:
                    for row in grid:
                        for cell in row:
                            cell.update_neighbors(grid)

                    a_star(lambda: draw(screen, grid, ROWS, width),
                           grid, start, end, euclidean_distance)

                elif event.key == pygame.K_3 and start and end:
                    for row in grid:
                        for cell in row:
                            cell.update_neighbors(grid)

                    a_star(lambda: draw(screen, grid, ROWS, width),
                           grid, start, end, chebyshev_distance)

                elif event.key == pygame.K_4 and start and end:
                    for row in grid:
                        for cell in row:
                            cell.update_neighbors(grid)

                    a_star(lambda: draw(screen, grid, ROWS, width),
                           grid, start, end, diagonal_distance)

                elif event.key == pygame.K_5 and start and end:
                    for row in grid:
                        for cell in row:
                            cell.update_neighbors(grid)

                    a_star(lambda: draw(screen, grid, ROWS, width),
                           grid, start, end, octile_distance)

                if event.key == pygame.K_c:
                    start = None
                    end = None
                    grid = make_grid(ROWS, width)

    pygame.quit()


if __name__ == "__main__":
    main(SCREEN, WIDTH)
