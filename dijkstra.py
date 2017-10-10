from queues import PriorityQueue


def djikstra(start_tile, end_tile):
    """
    Dijkstra's algorithm
    :param start_tile: Tile object, start tile of board
    :param end_tile: Tile object, end tile of board
    :return:
    """
    queue = PriorityQueue()
    queue.put(start_tile, 0)
    came_from = {start_tile: None}
    cost_so_far = {start_tile: 0}
    has_been_next_tile = []

    while not queue.empty():
        current_tile = queue.get()
        current_tile.visit()

        if current_tile == end_tile:
            break

        for next_tile in current_tile.neighbours:
            if next_tile not in has_been_next_tile:
                has_been_next_tile.append(next_tile)
            new_cost = cost_so_far[current_tile] + next_tile.weight

            if next_tile not in cost_so_far or new_cost < cost_so_far[next_tile]:
                cost_so_far[next_tile] = new_cost

                priority = new_cost
                queue.put(next_tile, priority)

                came_from[next_tile] = current_tile

    return came_from, cost_so_far, has_been_next_tile

