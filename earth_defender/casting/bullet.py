from .actor import Actor
from constants import *


class Bullet(Actor):
    """Bullet class performs all things needed to make, 
    shoot, and track collisions of a bullet

    Attributes:
        Inherited from Actor:
            _text (string): The text to display
            _font_size (int): The font size to use.
            _color (Color): The color of the text.
            _position (Point): The screen coordinates.
            _velocity (Point): The speed and direction.
    """

    def __init__(self):
        """Constructs a new Bullet."""
        super().__init__()

    # Get the bullets list from cast
    # Grab a bullet from the bullets list at index self._counter
    # Set the color, and position of the bullet
    def create_bullet(self, cast):
        """Creates bullets and sets their position equal to the 
        player's current position

        Args:
            cast (Cast): The cast of all actors.
        """
        new_bullet = Bullet()
        new_bullet.set_text("^")
        new_bullet.set_font_size(BULLET_SIZE)
        new_bullet.set_color(WHITE)
        # call player in order to set positon to bullet position
        player = cast.get_first_actor("player")
        new_bullet.set_position(player.get_position())
        # add bullet to cast for use throughout
        cast.add_actor("bullets", new_bullet)

    def move_next(self):
        """Moves the bullet one space up."""
        self._position.y -= 8
