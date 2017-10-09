import math

class Tile (object):

    def __init__(self, type, x_cord, y_cord):

        self.neighbours = []

        #Init tile variables
        self.type = type
        self.x_cord = x_cord
        self.y_cord = y_cord
        self.visited = False
        self.start = False
        self.end = False

        #Cordinates for drawing rectangles
        self.x1 = self.y_cord * 20
        self.x2 = self.x1 + 20
        self.y1 = self.x_cord * 20
        self.y2 = self.y1 + 20

        #Give tile a weight depending on type
        if(type in ['.', 'r', 'g', 'f', 'm', 'w', '#', 'A', 'B']):
            self.weight = {
            '.': 0,
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
                '.': '#cbe079',
                'r': '#fdd692',
                'g': "#64bd1f",
                'f': "#287c50",
                'm': "#aaaaaa",
                'w': "#47a2bd",
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
        Visit node
        :return: None
        '''
        self.visited = True
        self.color = "grey"

    def __str__(self):
        '''
        To String for tile
        :return: String representation of a tile
        '''

        return 'Tile: (' + str(self.x_cord) + "," + str(self.y_cord) + "), " \
               + "Visited: " + str(self.visited) \
               + ", Weight: " + str(self.weight) \
               + ", Type: " + str(self.type)