from tkinter import *

from tile import *
from bfs import *
from dijkstra import *
from a_star import *
from time import sleep


class Board(object):

    def __init__(self, pathname, algo):

        #Get board and set hight/width
        self.pathname = pathname
        self.board = self.get_file_as_list(self.get_file(pathname))
        self.height = len(self.board)
        self.width = len(self.board[0])

        #Init list and dictionary for tiles
        self.tiles = {}
        self.tiles_list = []

        #Generate board with canvas for visualization, add title with board and algorithm
        self.root = Tk()
        self.root.title(pathname[7:-4] + "' " + algo)
        self.canvas = Canvas(self.root, width=self.width*30, height=self.height * 30, highlightthickness=0)

        #Start and end tiles plus cost
        self.start_tile = None
        self.end_tile = None
        self.cost = 0

        #Generate tiles and visualize board with given colors depending on type
        self.generate_tiles()
        self.draw_board()

        #Create a graph over tiles
        self.map_neighbours()

        #Run algorithm with given algorithm
        self.root.attributes('-topmost', True)
        self.run_algorithm(algo)
        self.root.attributes('-topmost', 0)

        if algo == 'bfs':
            self.root.title("Board: " + pathname[13:-4] + ", Algorithm: " + "Breadth-first search")

        else:
            self.root.title("Board: " + pathname[13:-4] + ", Algorithm: " + algo + ", Cost: " + str(self.cost))

        #Keep window open after finish
        self.root.mainloop()


    def run_algorithm(self, algo):
        """
        Main algorithm function.
        :param algo: String, choosen algorithm
        :return: None
        """

        #Breadth-first search algorithm
        if algo == 'bfs':

            cf,hbxt = bfs(self.start_tile, self.end_tile)

        #Dijkstra's algorithm
        elif algo == 'dijkstra':
            cf, csf, hbxt = dijkstra(self.start_tile, self.end_tile)
            self.cost = csf[self.end_tile]

        #A* algorithm
        elif algo == 'a_star':
            cf, csf, hbxt = a_star(self.start_tile, self.end_tile)
            self.cost = csf[self.end_tile]

        self.draw_paths(cf, hbxt, algo)


    def draw_paths(self, cf, hbxt, algo):
        """
        Change color of visited tiles, draw shortest path and tiles that has been considered but not visited
        :param cf: Dictionary, containing a dictionary with tiles that been visited from start to end
        :param hbxt: List, containing a list of the shortest path from start to end
        :return: None
        """

        #Draw visited nodes
        for tile, came_from in cf.items():
            if came_from is None:
                pass
            else:
                if (tile.type == 'B'):
                    break
                elif(tile.visited):
                    self.root.after(25, self.update_board(tile, "visited"))
                    self.root.update()

        #Draw evaluated but not visited tiles
        for tile in hbxt:

            if (tile.type != 'B' and tile.type != 'A' and not tile.visited):
                self.root.after(25, self.update_board(tile,"been_next"))
                self.root.update()

        #Draw shortest path

        path = self.reconstruct_path(cf)

        for tile in path:

            self.root.after(25, self.update_board(tile, None))

    def map_neighbours(self):
        """
        Mapping neighbours to tiles
        :return: None
        """
        for key, tile in self.tiles.items():
            r, c = tile.x_cord, tile.y_cord

            #Tile is top left
            if(r == 0 and c == 0):
                self.add_neighbours(tile, self.tiles[r+1, c])     #Under
                self.add_neighbours(tile, self.tiles[r, c+1])     #Right

            #Tile is top right
            elif(r == 0 and c == self.width-1):
                self.add_neighbours(tile, self.tiles[r+1,c])      #Under
                self.add_neighbours(tile, self.tiles[r, c-1])     #Left

            #Tile is bottom left
            elif(r == self.height-1 and c == 0):
                self.add_neighbours(tile, self.tiles[r-1, c])     #Top
                self.add_neighbours(tile, self.tiles[r, c+1])     #Right

            #Bottom right
            elif(r == self.height-1 and c == self.width-1):
                self.add_neighbours(tile, self.tiles[r-1,c])      #Top
                self.add_neighbours(tile, self.tiles[r, c-1])     #Left

            #Top border
            elif(r == 0):
                self.add_neighbours(tile, self.tiles[r, c-1])     #Left
                self.add_neighbours(tile, self.tiles[r+1,c])      #Under
                self.add_neighbours(tile, self.tiles[r, c+1])     #Right

            #Right border:
            elif(c == self.width-1):
                self.add_neighbours(tile, self.tiles[r-1,c])      #Top
                self.add_neighbours(tile, self.tiles[r+1, c])     #Under
                self.add_neighbours(tile, self.tiles[r, c-1])     #Left
            #Bottom border
            elif(r == self.height-1):
                self.add_neighbours(tile, self.tiles[r-1, c])     #Top
                self.add_neighbours(tile, self.tiles[r, c-1])     #Left
                self.add_neighbours(tile, self.tiles[r, c+1])     #Right

            #Left border
            elif(c == 0):
                self.add_neighbours(tile, self.tiles[r-1, c])     #Top
                self.add_neighbours(tile, self.tiles[r, c+1])     #Right
                self.add_neighbours(tile, self.tiles[r+1, c])     #Under

            else:
                self.add_neighbours(tile, self.tiles[r-1,c])      #Top
                self.add_neighbours(tile, self.tiles[r, c+1])     #Right
                self.add_neighbours(tile, self.tiles[r+1, c])     #Under
                self.add_neighbours(tile, self.tiles[r, c-1])     #Left

    def add_neighbours(self, tile1, tile2):
        """
        Setting neighbour relation between two tiles
        :param tile1: Tile object
        :param tile2: Tile object
        :return: None
        """

        if tile2.type != '#':
            if tile2 not in tile1.neighbours:
                tile1.neighbours.append(tile2)
        if tile1.type != '#':

            if tile1 not in tile2.neighbours:
                tile2.neighbours.append(tile1)

    def reconstruct_path(self, came_from):
        """
        Reconstruct the shortest path from start to end
        :param came_from: List
        :return: None
        """
        current = self.end_tile
        path = [current]

        while current != self.start_tile:
            current = came_from[current]

            path.append(current)

        path.append(self.start_tile)
        path.reverse()

        return path

    @staticmethod
    def get_file(filepath):
        '''
        Get file
        :param filepath: String
        :return: file object
        '''
        return open(filepath)

    @staticmethod
    def get_file_as_list(file):
        '''
        Get file as a list
        :param file: file object
        :return: lines of chars as a list
        '''
        return file.read().splitlines()

    def generate_tiles(self):
        '''
        Generate tiles based on board list and add to a list and a dictionary
        :return: None
        '''
        for row in range (self.height):
            for col in range (self.width):
                t = Tile(self.board[row][col], row, col)
                self.tiles[row, col] = t
                self.tiles_list.append(t)
                if(t.type == 'A'): self.start_tile = t
                elif(t.type == 'B'): self.end_tile = t

    def draw_board(self):
        '''
        Draw the board with the given tiles and color
        :return: None
        '''

        for r in range(self.height):
            for c in range(self.width):
                t = self.tiles[r,c]
                self.canvas.create_rectangle(t.x1, t.y1, t.x2, t.y2, fill=t.color, outline='white')
        self.canvas.pack()

    def update_board(self, tile, sign):

        '''
        Update the board with a circle when visiting a tile
        :param tile: tile object
        :return: None
        '''
        if sign == "visited":
        #If not start title, don't draw dot
            if (tile.type != 'B' and tile.type != 'A' or tile.visited):
                self.canvas.create_rectangle(tile.x1, tile.y1, tile.x2, tile.y2, fill=tile.color_visited, outline='black')
                #self.canvas.create_oval(tile.x1 + 7, tile.y1 + 7, tile.x2 - 7, tile.y2 - 7, fill="#777777", outline="")


        elif sign == "been_next":
            self.canvas.create_oval(tile.x1 + 10, tile.y1 + 10, tile.x2 - 10, tile.y2 - 10, fill="white", outline="black")

        else:
            # If not start title, don't draw dot
            if (not tile.start or not tile.end):
                self.canvas.create_oval(tile.x1 + 10, tile.y1 + 10, tile.x2 - 10, tile.y2 - 10, fill="black", outline="white")


        self.canvas.update()

b = Board('boards/board-2-2.txt', "a_star")
