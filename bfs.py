from queue import Queue

def bfs(start_tile, end_tile):
    queue = Queue()
    queue.put(start_tile)
    came_from = {}
    came_from[start_tile] = None

    while not queue.empty():
        current_tile = queue.get()

        if current_tile == end_tile:
            print(current_tile)
            break

        for tile in current_tile.neighbours:

            if tile not in came_from:
                queue.put(tile)
                came_from[tile] = current_tile
                print(current_tile)
                current_tile.visit()


    return came_from