import heapq
from Grid import *
from Cell import *
from heuristics import *


def astar(grid, start, end, heuristic):
    open_list = []
    closed_set = set()
    g_scores = {start: 0}
    f_scores = {start: heuristic(start, end)}
    came_from = {}

    heapq.heappush(open_list, (f_scores[start], start))

    while open_list:
        current = heapq.heappop(open_list)[1]

        if current == end:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path

        closed_set.add(current)

        for neighbor in grid.get_neighbors(current):
            tentative_g_score = g_scores[current] + 1

            if neighbor in closed_set and tentative_g_score >= g_scores.get(neighbor, float('inf')):
                continue

            if tentative_g_score < g_scores.get(neighbor, float('inf')):
                came_from[neighbor] = current
                g_scores[neighbor] = tentative_g_score
                f_scores[neighbor] = tentative_g_score + \
                    heuristic(neighbor, end)
                if neighbor not in closed_set:
                    heapq.heappush(open_list, (f_scores[neighbor], neighbor))

        # print actual distances
        print("Euclidean: ", euclidean_distance(current, end))
        print("Manhattan: ", manhattan_distance(current, end))

    return None
