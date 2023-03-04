import pygame
import numpy as np
from square import Square
from ball import Ball
class Board:
    def __init__(self, width, height,boardChoosen):
        self.width = width
        self.height = height
        self.tile_width = width // boardChoosen.shape[1] #the tile's size will depend of the board size chosen
        self.tile_height = height // boardChoosen.shape[1]
        self.selected_piece = None
        self.board = boardChoosen
        self.div=boardChoosen.shape[1]//3
        self.turn = 'red'
        self.squares = self.generate_squares()
        self.setup_board()

    def generate_squares(self):
        board = []
        for y in range(self.board.shape[0]):
            for x in range(self.board.shape[0]):
                board.append(
                    Square(x,  y, self.tile_width, self.tile_height, self.board[x][y])
                )
        return board
    

    def get_square_from_pos(self, pos):
        for square in self.squares:
            if (square.x, square.y) == (pos[0], pos[1]):
                return square
            
    def get_piece_from_pos(self, pos):
        return self.get_square_from_pos(pos).occupying_piece
    

    def setup_board(self):
        for y, row in enumerate(self.board):
            for x, piece in enumerate(row):
                if piece != 0:
                    square = self.get_square_from_pos((x, y))
                    # looking inside contents, what piece does it have
                    if piece == 1: #Player 1 is the blue ball
                        square.occupying_piece = Ball(
                            (x, y), 'blue', self
                        )
                    # as you notice above, we put `self` as argument, or means our class Board
                    elif piece == 2: # Player 2 is the green ball
                        square.occupying_piece = Ball(
                            (x, y), 'red', self
                        )
                    elif piece==3:
                        square.occupying_piece = Ball(
                            (x, y), 'white', self
                        )

    def draw(self, display):
        if self.selected_piece is not None:
            #self.get_square_from_pos(self.selected_piece.pos).highlight = True
          #  print(list)
            for square in self.selected_piece.get_moves(self):
                #print(square)
                square.highlight = True
        for square in self.squares:
            square.draw(display)

    def handle_click(self, mx, my):
        x = mx // self.tile_width
        y = my // self.tile_height
        clicked_square = self.get_square_from_pos((x, y))
        #print(clicked_square.x, clicked_square.y)
        if self.selected_piece is None:
            if clicked_square.occupying_piece is not None:
                if clicked_square.occupying_piece.color == self.turn:
                    self.selected_piece = clicked_square.occupying_piece 
        elif self.selected_piece.move(self, clicked_square):
            self.turn = 'blue' if self.turn == 'red' else 'red'
            
"""     def is_in_checkmate(self, color):
	    output = False
        for piece in [i.occupying_piece for i in self.squares]:
		    if piece != None:
			    if piece.notation == 'K' and piece.color == color:
				    king = piece


		    if king.get_valid_moves(self) == []:
		        if self.is_in_check(color):
				    output = True

	    return output """

    

