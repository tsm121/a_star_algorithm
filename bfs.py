from queues import Queue


def bfs(start_tile, end_tile):
    """
    Breadth-first search algorithm
    :param start_tile: Tile object, start tile of board
    :param end_tile: Tile object, end tile of board
    :return:
    """
    queue = Queue()
    queue.put(start_tile)
    came_from = {}
    came_from[start_tile] = None
    has_been_next_tile = []

    while not queue.empty():
        current_tile = queue.get()
        current_tile.visit()

        if current_tile == end_tile:
            break

        for next_tile in current_tile.neighbours:

            if next_tile not in has_been_next_tile:
                has_been_next_tile.append(next_tile)


            if next_tile not in came_from:
                queue.put(next_tile)
                came_from[next_tile] = current_tile
                current_tile.visit()

    return came_from, has_been_next_tile