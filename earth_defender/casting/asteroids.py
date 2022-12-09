from .actor import Actor


class Asteroids(Actor):
    """An asteroid is a falling object, represented by an asterisk, that the player attempts to shoot to keep it from hitting the ground.

    Attributes:
        Inherited from Actor:
            _text (string): The text to display
            _font_size (int): The font size to use.
            _color (Color): The color of the text.
            _position (Point): The screen coordinates.
            _velocity (Point): The speed and direction.
    """

    def __init__(self):
        """Constructs a new Asteroid."""
        super().__init__()

    def asteroid_bullet(self):
        """Finds the point of the object

        Returns:
            Point: The point of the object.
        """
        return self._point

    def get_item_type(self):
        """Gets the item type.

        Returns:
            string: The item type.
        """
        return self._object

    def move_next(self, speed):
        """Moves the asteroid one space down.

        Args:
            speed (int): The speed at which the asteroid falls.
        """
        if self._move_counter < 2:
            self._move_counter += 1
        else:
            self._position.y += speed
            self._move_counter = 0
