from .actor import Actor
from constants import *
from ..shared.point import Point


class Message(Actor):
    """The Message is a display to the user that will show the user a message on screen.  
    Attributes:
        Inherited from Actor:
            _text (string): The text to display
            _font_size (int): The font size to use.
            _color (Color): The color of the text.
            _position (Point): The screen coordinates.
            _velocity (Point): The speed and direction.
    """
    
    def __init__(self):
        super().__init__()

    def create_message(self, cast):
        message = Message()
        # Sets the postion of the game over text
        message.set_text(GAME_OVER_MESSAGE_TEXT)
        message.set_position(GAME_OVER_MESSAGE_POSITION)
        cast.add_actor("messages", message)
        