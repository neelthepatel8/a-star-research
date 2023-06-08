class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.f_score = 0

    def __hash__(self):
        return hash((self.row, self.col))

    def __eq__(self, other):
        return self.row == other.row and self.col == other.col

    def __lt__(self, other):
        return self.f_score < other.f_score

    def __repr__(self):
        return f"({self.row}, {self.col})"
