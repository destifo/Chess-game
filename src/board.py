

from const import *
from piece import *
from square import Square


class Board:

    def __init__(self) -> None:
        self.squares = [[0 for i in range(COLS)] for j in range(ROWS)]

        self._create()
        self._addPieces('white')
        self._addPieces('black')

    def _create(self) -> None:
        for row in range(ROWS):
            for col in range(COLS):
                self.squares[row][col] = Square(row, col)

    
    def calcMoves(self, piece):


        def knightMoves(row: int, col: int):
            possible_moves = [
                (row-2, col-1),
                (row-2, col+1),
                (row+1, col+2),
                (row+1, col-2),
                (row+2, col+1),
                (row+2, col-1),
                (row+1, col+2),
                (row+1, col-2),
            ]

            for move in possible_moves:
                move_row, move_col = move
                if not Square.inRange(move_row, move_col):  continue


        if isinstance(piece, Pawn):
            pass

        if isinstance(piece, Knight):
            pass

        if isinstance(piece, Bishop):
            pass

        if isinstance(piece, Rook):
            pass

        if isinstance(piece, Queen):
            pass


    def _addPieces(self, color):
        squares = self.squares

        pawn_row, others_row = (1, 0) if color == 'black' else (6, 7)

        # add pawns
        for col in range(COLS):
            squares[pawn_row][col] = Square(pawn_row, col, Pawn(color))
        
        # add rooks
        squares[others_row][0], squares[others_row][7] = Square(pawn_row, col, Rook(color)), Square(pawn_row, col, Rook(color))

        # add knights
        squares[others_row][1], squares[others_row][6] = Square(pawn_row, col, Knight(color)), Square(pawn_row, col, Knight(color))

        # add bishops
        squares[others_row][2], squares[others_row][5] = Square(pawn_row, col, Bishop(color)), Square(pawn_row, col, Bishop(color))

        # add z queen
        squares[others_row][3] = Square(pawn_row, col, Queen(color))
        
        # add z king
        squares[others_row][4] = Square(pawn_row, col, King(color))

