import collections

#A simple Queue class
class Queue():
    def __init__(self):
        self.elements = collections.deque()

    def empty(self):
        return len(self.elements) == 0

    def put(self, tile):
        self.elements.append(tile)

    def get(self):
        return self.elements.popleft()

import heapq

#A simple priority queue class
class PriorityQueue():

    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def put(self, tile, weight):
        heapq.heappush(self.elements, (weight, tile))

    def get(self):
        return heapq.heappop(self.elements)[1]

    def __len__(self):
        return len(self.elements)

