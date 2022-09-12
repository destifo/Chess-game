import pygame
import sys

from const import *
from game import Game

class Main:

    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Chess')
        self.game = Game()

    def mainloop(self) -> None:
        game = self.game
        dragger = game.dragger
        board = game.board
        screen = self.screen
        
        while True:
            game.drawBG(screen)
            game.drawPieces(screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # click
                if event.type == pygame.MOUSEBUTTONDOWN:
                    dragger.updateMouse(event.pos)

                    clicked_row = dragger.mouseY // SQSIZE
                    clicked_col = dragger.mouseX // SQSIZE

                    if board.squares[clicked_row][clicked_col].hasPiece:
                        piece =  board.squares[clicked_row][clicked_col].piece
                        dragger.saveInitial(event.pos)

                # hover
                if event.type == pygame.MOUSEMOTION:
                    pass

                # release click
                if event.type == pygame.MOUSEBUTTONUP:
                    pass

            

            pygame.display.update()


main = Main()
main.mainloop()