from ..shared.point import Point
from ..casting.bullet import Bullet
from ..shared.point import Point
import pyray
from constants import *


class KeyboardService:
    """Detects player input. 

    The responsibility of a KeyboardService is to detect player key presses and translate them into 
    a point representing a direction.

    Attributes:
        cell_size (int): For scaling directional input to a grid.
    """

    def __init__(self, cell_size=1):
        """Constructs a new KeyboardService using the specified cell size.

        Args:
            cell_size (int): The size of a cell in the display grid.
        """
        self._cell_size = cell_size

    # Passing the player and cast objects from Main to keyboard_service
    def add_player(self, cast, player):
        self._cast = cast
        self._player = player

    def get_direction(self):
        """Gets the selected direction based on the currently pressed keys.

        Returns:
            Point: The selected direction.
        """
        dx = 0
        dy = 0

        if pyray.is_key_down(pyray.KEY_LEFT):
            dx = -1

        if pyray.is_key_down(pyray.KEY_RIGHT):
            dx = 1

        direction = Point(dx, dy)
        direction = direction.scale(self._cell_size)

        return direction

    def get_play_again(self):
        """Allows the player specify whether to play again.

        Returns:
            bool: True if the player wants to play again, False otherwise.
        """
        was_pressed = False
        if pyray.is_key_released(pyray.KEY_Y):
            was_pressed = True
        else:
            was_pressed = False

        return was_pressed
    

    def make_bullet(self, cast):
        if pyray.is_key_pressed(pyray.KEY_SPACE):
            bullet = Bullet()
            bullet.create_bullet(cast)
