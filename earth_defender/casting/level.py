from ..casting.actor import Actor


class Level(Actor):
    """The level is an integer that controls the speed
    at which the astroids fall to earth. It also controls
    the number of astroids that will fall to earth in order
    to advance to the next level.

    Attributes:
        Inherited from Actor:
            _text (string): The text to display
            _font_size (int): The font size to use.
            _color (Color): The color of the text.
            _position (Point): The screen coordinates.
    """

    def __init__(self):
        """Constructor for the Level class."""
        super().__init__()
        self._level = 1

    def level_up(self):
        """Increases the level by 1 and increases the speed
        at which the astroids fall to earth.

        Returns:
            int: The current level.
        """
        self._level += 1

        return self._level

    def reset_level(self):
        """Resets the level to 1."""
        self._level = 1
