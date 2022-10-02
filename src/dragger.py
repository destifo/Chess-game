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

    
    def updateBlit(self, surface) -> None:
        # texture/image url
        self.piece.setImage(128)
        img_url = self.piece.image_url
        
        #image
        img = pygame.image.load(img_url)

        #centering
        img_center = (self.mouseX, self.mouseY)
        self.piece.tex_rect = img.get_rect(center=img_center)

        # draw the piece
        surface.blit(img, self.piece.tex_rect)



    def updateMouse(self, pos) -> None:
        self.mouseX, self.mouseY = pos

    def saveInitial(self, pos) -> None:
        self.initial_row = pos[1] // SQSIZE
        self.initial_col = pos[0] // SQSIZE

    def dragPiece(self, piece):
        self.piece = piece
        self.dragging = True

    def unDragPiece(self):
        self.piece.setImage(80)
        self.piece = None
        self.dragging = False