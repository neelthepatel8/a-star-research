from Cell import Cell
import matplotlib.pyplot as plt


class Grid:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.cells = [[0 for _ in range(cols)] for _ in range(rows)]

    def set_cell(self, cell, value):
        self.cells[cell.row][cell.col] = value

    def get_cell(self, cell):
        return self.cells[cell.row][cell.col]

    def is_valid(self, cell):
        return cell.row >= 0 and cell.row < self.rows and cell.col >= 0 and cell.col < self.cols and self.cells[cell.row][cell.col] != 1

    def get_neighbors(self, cell):
        neighbors = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                neighbor = Cell(cell.row + i, cell.col + j)
                if self.is_valid(neighbor):
                    neighbors.append(neighbor)
        return neighbors

    def visualize_path(self, start, end, path):
        fig, ax = plt.subplots(figsize=(self.cols / 2, self.rows / 2))

        ax.scatter(start.col + 0.5, start.row + 0.5, color='green', s=100)
        ax.scatter(end.col + 0.5, end.row + 0.5, color='red', s=100)

        x_vals = [cell.col + 0.5 for cell in path]
        y_vals = [cell.row + 0.5 for cell in path]
        ax.plot(x_vals, y_vals, color='blue')

        for row in range(self.rows):
            for col in range(self.cols):
                if self.cells[row][col] == 1:
                    ax.add_patch(plt.Rectangle(
                        (col, row), 1, 1, color='black'))

        ax.set_xlim(0, self.cols)
        ax.set_ylim(self.rows, 0)

        plt.show()
