import pygame

from const import *

class Dragger:

    def __init__(self) -> None:
        self.mouseX = 0
        self.mouseY = 0

        self.piece = None
        self.dragging = False
        
        self.initial_row = 0
        self.initial_col = 0

    def updateMouse(self, pos) -> None:
        self.mouseX, self.mouseY = pos

    def saveInitial(self, pos) -> None:
        self.initial_row = pos[1] // SQSIZE
        self.initial_col = pos[0] // SQSIZE

    def dragPiece(self, piece):
        self.piece = piece
        self.dragging = True

    def unDragPiece(self):
        self.piece = None
        self.dragging = False