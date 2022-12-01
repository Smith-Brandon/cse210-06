from .actor import Actor
from ..shared.point import Point


class Objects(Actor):
    """
    An item of cultural or historical interest. 

    The responsibility of an Artifact is to provide a message about itself.

    Attributes:
        _message (string): A short description about the artifact.
    """

    def __init__(self):
        super().__init__()
        self._message = ""
        self._move_counter = 0
        self._velocity = Point(0, 0)

    def asteroid_bullet(self):
        return self._point

    def get_item_type(self):
        return self._object

    def fall(self, speed=1):
        if self._move_counter < 2:
            self._move_counter += 1
        else:
            self._position.y += speed
            self._move_counter = 0

# Move the bullet one space up
    def shoot(self):
        if self._move_counter < 2:
            self._move_counter += 1 
        else:
            self._position.y -= 1
            self._move_counter = 0

