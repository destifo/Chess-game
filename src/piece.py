import os


class Piece:

    def __init__(self, name, color, value, image_url=None, tex_rect=None) -> None:
        self.name = name
        self.color = color
        
        value_sign = 1 if color == 'white' else -1
        self.value = value * value_sign

        self.moves = []
        self.moved = False
        
        self.image_url = image_url
        self._setImage()
        self.tex_rect = tex_rect

    
    def _setImage(self, size=80) -> None:
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        self.image_url = os.path.join(
            f'../assets/images/imgs-{size}px/{self.color}_{self.name}.png'
        )

    def add_move(self, move):
        self.moved = False
        self.moves.append(move)


class Pawn(Piece):

    def __init__(self, color) -> None:
        self.dir = -1 if color == 'white' else 1
        super().__init__('pawn', color, 1.0)


class Knight(Piece):

    def __init__(self, color) -> None:
        super().__init__('knight', color, 3.0)


class Bishop(Piece):

    def __init__(self, color) -> None:
        super().__init__('bishop', color, 3.0)

    
class Rook(Piece):

    def __init__(self, color) -> None:
        super().__init__('rook', color, 5.0)

    
class Queen(Piece):

    def __init__(self, color) -> None:
        super().__init__('queen', color, 9.0)


class King(Piece):

    def __init__(self, color) -> None:
        super().__init__('king', color, float('inf'))