import math


def manhattan_h(node, goal):
    return abs(node.row - goal.row) + abs(node.col - goal.col)


def euclidian_h(node, goal):
    x_diff = abs(node.row - goal.row)
    y_diff = abs(node.col - goal.col)
    return math.sqrt(x_diff ** 2 + y_diff ** 2)


def diagonal_h(node, goal):
    x_diff = abs(node.row - goal.row)
    y_diff = abs(node.col - goal.col)
    return max(x_diff, y_diff)


def octile_h(node, goal):
    dx = abs(node.row - goal.row)
    dy = abs(node.col - goal.col)
    D = math.sqrt(2)
    return (dx + dy) + (D - 2) * min(dx, dy)
