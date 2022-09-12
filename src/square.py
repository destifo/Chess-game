


from tkinter import PIESLICE


class Square:

    def __init__(self, row, col, piece=None) -> None:
        self.row = row
        self.col = col
        self.piece = piece

    def hasPiece(self):
        return self.piece != None
