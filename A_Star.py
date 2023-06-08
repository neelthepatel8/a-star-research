from queue import PriorityQueue
import timeit
from functools import partial


def make_path(came_from, current):
    path = []
    while current in came_from:
        current = came_from[current]
        path.append(current)

    path.reverse()
    return path


def A_Star(grid, start, end, h):
    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, start))
    came_from = {}
    g_score = {cell: float("inf") for row in grid for cell in row}
    g_score[start] = 0
    f_score = {cell: float("inf") for row in grid for cell in row}
    f_score[start] = h(start, end)

    open_set_hash = {start}
    nodes_looked_at = 0

    while not open_set.empty():

        current = open_set.get()[2]
        open_set_hash.remove(current)

        if current == end:
            return make_path(came_from, end), nodes_looked_at

        for neighbor in current.neighbors:
            temp_g_score = g_score[current] + 1

            if temp_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = temp_g_score + \
                    h(neighbor, end)
                if neighbor not in open_set_hash:
                    count += 1
                    open_set.put((f_score[neighbor], count, neighbor))
                    open_set_hash.add(neighbor)
                    neighbor.make_open()
                    neighbor.make_expanded()

        if current != start:
            current.make_closed()
        nodes_looked_at += 1

    return None, nodes_looked_at


def time_a_star(n, grid, start, end, h):
    astar = partial(A_Star, grid=grid, start=start, end=end, h=h)
    time_taken = timeit.timeit(astar, number=n)
    return time_taken
