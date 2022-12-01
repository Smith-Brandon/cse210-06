from ..shared.point import Point
from ..casting.objects import Objects
from ..shared.color import Color
from ..shared.point import Point
import pyray

BULLET_SIZE = 30
WHITE = Color(255, 255, 255)
COUNTER = 0


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
        self._counter = COUNTER

    # Passing the player and cast objects from Main to keyboard_service
    def add_player(self, cast, player):
        self._cast = cast
        self._player = player

    # Move the bullet position above the player
    def move_position(self, position):
        pos = position
        x = pos.get_x()
        y = pos.get_y()
        y = y - 10
        return Point(x, y)

# Get the bullets list from cast
# Grab a bullet from the bullets list at index self._counter
# Set the color, and position of the bullet
    def create_bullet(self):
        bullets = self._cast.get_actors("bullets")
        bullet = bullets[self._counter]
        self._counter = self._counter + 1

        bullet.set_color(WHITE)
        bullet.set_position(self.move_position(self._player.get_position()))

        if self._counter == 49:
            self._counter = 0

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

        # If space is pressed, call the create_bullet function
        if pyray.is_key_pressed(pyray.KEY_SPACE):
            self.create_bullet()
        '''
        if pyray.is_key_down(pyray.KEY_UP):
            dy = -1
        
        if pyray.is_key_down(pyray.KEY_DOWN):
            dy = 1
        '''
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
