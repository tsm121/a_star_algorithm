import math

class Tile (object):

    def __init__(self, type, x_cord, y_cord):
        """
        A tile class for representing the given boards
        :param type: Char, contains the type of the tile
        :param x_cord: Int, x-coordinate for tile
        :param y_cord: Int, y-coordinate for tile
        """

        self.neighbours = []

        #Init tile variables
        self.type = type
        self.x_cord = x_cord
        self.y_cord = y_cord
        self.visited = False
        self.start = False
        self.end = False

        #Cordinates for drawing rectangles
        self.x1 = self.y_cord * 30
        self.x2 = self.x1 + 30
        self.y1 = self.x_cord * 30
        self.y2 = self.y1 + 30

        #Give tile a weight depending on type
        if(type in ['.', 'r', 'g', 'f', 'm', 'w', '#', 'A', 'B']):
            self.weight = {
            '.': 1,
            'r': 1,
            'g': 5,
            'f': 10,
            'm': 50,
            'w': 100,
            '#': math.inf,
            'A': 0,
            'B': 0
        }[type]

            #Set tile color depending on type
            self.color = {
                '.': '#EBE6EE', #
                'r': '#6E4C39', #
                'g': "#89C92A", #
                'f': "#4B7F52", #
                'm': "#E0C5AA", #
                'w': "#4091CF", #
                '#': "black",
                'A': 'red',
                'B': 'blue'
            }[type]

        # Set tile color depending on type
        self.color_visited = {
            '.': '#D7D6D7', #
            'r': '#533E2C', #
            'g': "#608725", #
            'f': "#196823", #
            'm': "#AD8F70", #
            'w': "#0A68AF", #
            '#': "black",
            'A': 'red',
            'B': 'blue'
        }[type]

        #If start tile, set value to true
        if (type == 'A'):
            self.start = True

        #If end tile, set value to true
        elif (type == 'B'):
            self.end = True

    def visit(self):
        '''
        Visit node, set visited to True
        :return: None
        '''
        self.visited = True
        self.color = "grey"

    def __lt__(self, other):
        """
        Comparison method for two tiles
        :param other:
        :return:
        """
        return self.weight < other.weight

    def __str__(self):
        '''
        To String for tile
        :return: String representation of a tile
        '''

        return 'Tile: (' + str(self.x_cord) + "," + str(self.y_cord) + "), " \
               + "Visited: " + str(self.visited) \
               + ", Weight: " + str(self.weight) \
               + ", Type: " + str(self.type)