from tkinter import *

from tile import *
from bfs import *
from time import sleep


class Board(object):

    def __init__(self, pathname):

        #Get board and set hight/width
        self.pathname = pathname
        self.board = self.get_file_as_list(self.get_file(pathname))
        self.height = len(self.board)
        self.width = len(self.board[0])

        #Init list and dictionary for tiles
        self.tiles = {}
        self.tiles_list = []

        #Generate board with canvas for visualization
        self.root = Tk()
        self.root.title("A* algorithm  '" + pathname[7:-4] + "'")
        self.canvas = Canvas(self.root, width=self.width*20, height=self.height * 20, highlightthickness=0)

        #Start and end tiles for the A* algorithm
        self.start_tile = None
        self.end_tile = None

        #Generate tiles and visualize board with given colors depending on type
        self.generate_tiles()
        self.draw_board()

        #Create a graph over tiles
        self.map_neighbours()

        self.run_bfs()

        #Run algorithm
        #self.run_algorithm(self.start_tile, self.end_tile)
        self.root.mainloop()

    def run_bfs(self):

        cf = bfs(self.start_tile, self.end_tile)

        #Draw visited nodes
        for tile, came_from in cf.items():
            if came_from is None:
                pass
            else:
                if (tile.type == 'B'):
                    break
                else:
                    self.root.after(50, self.update_board(tile, "visited"))

        #Draw back the shortest path
        current = cf[self.end_tile]
        while current != self.start_tile:

            self.root.after(25, self.update_board(current, None))
            current = cf[current]


    def map_neighbours(self):
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

        if tile2.type != '#':
            if tile2 not in tile1.neighbours:
                tile1.neighbours.append(tile2)
        if tile1.type != '#':

            if tile1 not in tile2.neighbours:
                tile2.neighbours.append(tile1)


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
            if(not tile.start):
                self.canvas.create_oval(tile.x1 + 7, tile.y1 + 7, tile.x2 - 7, tile.y2 - 7, fill="#999999", outline="")

            self.canvas.update()

        else:
            # If not start title, don't draw dot
            if (not tile.start):
                self.canvas.create_oval(tile.x1 + 7, tile.y1 + 7, tile.x2 - 7, tile.y2 - 7, fill="black", outline="")


            self.canvas.update()


    def run_algorithm(self, start_tile, end_tile):
        '''
        Run the A* algorithm and visit tile
        :param start_tile: tile object
        :param end_tile:  tile object
        :return: None
        '''

        start_cord = self.tiles_list.index(start_tile)

        while (True):

            for tile in self.tiles_list[start_cord:]:

                if(tile.type != 'A' and tile.type != 'B'):
                    tile.visit()
                else: print(tile)

                if (tile.end): return
                self.root.after(50, self.update_board(tile))





b = Board('boards/board-1-2.txt')
