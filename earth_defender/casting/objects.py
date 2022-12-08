from .actor import Actor
from ..shared.point import Point


class Objects(Actor):
    """A visible, moveable thing that participates
    in the game.
    """

    def __init__(self):
        """Constructor for the Objects class."""
        super().__init__()
        self._message = ""
        self._move_counter = 0
        self._velocity = Point(0, 0)

    def asteroid_bullet(self):
        """Gets the point value for the object.

        Returns:
            Point: The point value for the object.
        """
        return self._point

    def get_item_type(self):
        """Gets the item type for the object.

        Returns:
            string: The item type for the object.
        """
        return self._object

    def fall(self, speed=1):
        """Moves the object down one space.

        Args:
            speed (int): The speed of the object.
        """
        if self._move_counter < 2:
            self._move_counter += 1
        else:
            self._position.y += speed
            self._move_counter = 0

    def shoot(self):
        """Moves the object up one space."""
        self._position.y -= 8
