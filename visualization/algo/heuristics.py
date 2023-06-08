import math


def euclidean_distance(cell1, cell2):
    return math.sqrt((cell1.row - cell2.row)**2 + (cell1.col - cell2.col)**2)


def manhattan_distance(cell1, cell2):
    return abs(cell1.row - cell2.row) + abs(cell1.col - cell2.col)


# def manhattan_distance(current_x, current_y, goal_x, goal_y):
#     return abs(current_x - goal_x) + abs(current_y - goal_y)


# def euclidean_distance(current_x, current_y, goal_x, goal_y):
#     return math.sqrt((current_x - goal_x) ** 2 + (current_y - goal_y) ** 2)
