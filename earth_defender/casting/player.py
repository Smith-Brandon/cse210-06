from .actor import Actor
from constants import *
from ..shared.point import Point

class Player(Actor):
    """The Player is a character that moves side to side and can shoot bullets, represented by a hashtag.  
    Attributes:
        Inherited from Actor:
            _text (string): The text to display
            _font_size (int): The font size to use.
            _color (Color): The color of the text.
            _position (Point): The screen coordinates.
            _velocity (Point): The speed and direction.
    """

    def __init__(self):
        '''Cunstructs player'''
        super().__init__()

    def create_player(self, cast):
        '''Creates player and sets their position to the center of the screen on the bottom.
        
        Args:
            cast (Cast): The cast of all actors
        '''
        player = Player()
        position = Point(450, 575)

        player.set_text("#")
        player.set_font_size(PLAYER_SIZE)
        player.set_color(WHITE)
        player.set_position(position)
        cast.add_actor("player", player)
