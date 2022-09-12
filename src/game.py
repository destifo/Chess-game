import pygame
from board import Board

from const import *
from dragger import Dragger

class Game:

    def __init__(self) -> None:
        self.board = Board()
        self.dragger = Dragger()

    def drawBG(self, surface) -> None:
        for row in range(ROWS):
            for col in range(COLS):
                if (row + col) % 2 == 0:
                    color = (234, 235, 200)
                else:
                    color = (119, 154, 88)

                rect = (col * SQSIZE, row * SQSIZE, SQSIZE, SQSIZE)
                pygame.draw.rect(surface, color, rect)

    def drawPieces(self, surface):
        board = self.board

        for row in range(ROWS):
            for col in range(COLS):
                if board.squares[row][col].hasPiece():
                    piece = board.squares[row][col].piece
                    
                    img = pygame.image.load(piece.image_url)
                    img_center = col * SQSIZE + SQSIZE // 2, row * SQSIZE + SQSIZE // 2
                    piece.tex_rect = img.get_rect(center=img_center)
                    surface.blit(img, piece.tex_rect)


