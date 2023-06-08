import math


def manhattan_distance(current_x, current_y, goal_x, goal_y):
    return abs(current_x - goal_x) + abs(current_y - goal_y)


def euclidean_distance(current_x, current_y, goal_x, goal_y):
    return math.sqrt((current_x - goal_x) ** 2 + (current_y - goal_y) ** 2)


def octile_distance(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    return dx + dy + (math.sqrt(2) - 2) * min(dx, dy)


def diagonal_distance(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    return max(dx, dy) + (math.sqrt(2) - 1) * min(dx, dy)


def chebyshev_distance(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    return max(dx, dy)
