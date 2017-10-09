from tkinter import *

from tile import *
from time import sleep


class Board(object):

    def __init__(self, pathname):
        self.pathname = pathname
        self.board = self.get_file_as_list(self.get_file(pathname))
        self.height = len(self.board)
        self.width = len(self.board[0])
        self.tiles = {}
        self.root = Tk()


        self.generate_tiles()
        self.draw_board()


        while(True):
            for cord, tile in self.tiles.items():

                tile.visit()

                if (tile.end): return
                self.root.after(50, self.update_board(tile))

        self.root.mainloop()



    @staticmethod
    def get_file(filepath):
        return open(filepath)

    @staticmethod
    def get_file_as_list(file):
        return file.read().splitlines()

    def generate_tiles(self):
        for row in range (self.height):
            for col in range (self.width):
                self.tiles[row, col] = Tile(self.board[row][col], row, col)


    def draw_board(self):

        for r in range(self.height):
            for c in range(self.width):
                Canvas(self.root,bg=self.tiles[r, c].color ,width=20, height=20, highlightthickness=0).grid(column=c,row=r)

        # self.root.mainloop()
        self.root.update()

    def update_board(self, tile):


        x = tile.get_x_cord()
        y = tile.get_y_cord()
        print(x,y)
        print(tile)

        a = Canvas(self.root, bg = tile.color, width=20, height=20, highlightthickness=0)
        a.grid(column = y, row = x)
        a.update()

b = Board('boards/board-1-3.txt')
