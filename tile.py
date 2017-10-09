import math

class Tile (object):

    def __init__(self, type, x_cord, y_cord):

        self.type = type
        self.x_cord = x_cord
        self.y_cord = y_cord
        self.visited = False
        self.end = False

        if(type in ['.' , 'g', 'f', 'm', 'w', '#', 'A', 'B']):
            self.weight = {
            '.': 1,
            'g': 5,
            'f': 10,
            'm': 50,
            'w': 100,
            '#': math.inf,
            'A': 0,
            'B': 0
        }[type]

            self.color = {
                '.': '#cbe079',
                'g': "#cbe079",
                'f': "#69c13f",
                'm': "#754f44",
                'w': "#5bc0eb",
                '#': "#754f44",
                'A': 'red',
                'B': 'blue'
            }[type]


        if (type == 'B'):
            self.end = True

    def visit(self):
        self.visited = True
        self.color = "grey"


    def get_weight(self):
        return self.weight


    def get_x_cord(self):
        return self.x_cord

    def get_y_cord(self):
        return self.y_cord




    def __str__(self):

        return 'Tile: (' + str(self.x_cord) + "," + str(self.y_cord) + "), " \
               + "Visited: " + str(self.visited) \
               + ", Weight: " + str(self.weight) \
               + ", Type: " + str(self.type)