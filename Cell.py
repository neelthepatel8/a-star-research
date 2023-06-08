class Cell:
    def __init__(self, row, col, total_rows):
        self.row = row
        self.col = col
        self.neighbors = []
        self.total_rows = total_rows
        self.end = False
        self.start = False
        self.closed = False
        self.barrier = False
        self.open = False
        self.expanded = False

    def get_pos(self):
        return self.row, self.col

    def is_closed(self):
        return self.closed

    def is_open(self):
        return self.open

    def is_expanded(self):
        return self.expanded

    def is_barrier(self):
        return self.barrier

    def is_start(self):
        return self.start

    def is_end(self):
        return self.end

    def reset(self):
        self.end = False
        self.start = False
        self.closed = False
        self.barrier = False
        self.open = False
        self.expanded = False

    def make_start(self):
        self.start = True

    def make_expanded(self):
        self.expanded = True

    def make_closed(self):
        self.closed = True

    def make_open(self):
        self.open = True

    def make_barrier(self):
        self.barrier = True

    def make_end(self):
        self.end = True

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

    def __hash__(self):
        return hash(self.row + self.col)

    def __eq__(self, other):
        return self.row == other.row and self.col == other.col

    def __lt__(self, other):
        return False
