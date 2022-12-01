from ..shared.color import Color
from ..shared.point import Point


class Actor:
    """A visible, moveable thing that participates in the game. 
    
    The responsibility of Player is to keep track of its appearance, position and velocity in 2d 
    space.

    Attributes:
        _text (string): The text to display
        _font_size (int): The font size to use.
        _color (Color): The color of the text.
        _position (Point): The screen coordinates.
        _velocity (Point): The speed and direction.
    """

    def __init__(self):
        """Constructs a new Player."""
        self._text = ""
        self._font_size = 15
        self._color = Color(255, 255, 255)
        self._move_counter = 0
        self._position = Point(0, 0)
        self._velocity = Point(0, 0)

    def get_color(self):
        """Gets the player's color as a tuple of three ints (r, g, b).
        
        Returns:
            Color: The player's text color.
        """
        return self._color

    def get_font_size(self):
        """Gets the player's font size.
        
        Returns:
            Point: The player's font size.
        """
        return self._font_size

    def get_position(self):
        """Gets the player's position in 2d space.
        
        Returns:
            Point: The player's position in 2d space.
        """
        return self._position
    
    def get_text(self):
        """Gets the player's textual representation.
        
        Returns:
            string: The player's textual representation.
        """
        return self._text

    def get_velocity(self):
        """Gets the player's speed and direction.
        
        Returns:
            Point: The player's speed and direction.
        """
        return self._velocity
    
    def move_next(self, max_x, max_y):
        """Moves the player to its next position according to its velocity. Will wrap the position 
        from one side of the screen to the other when it reaches the given maximum x and y values.
        
        Args:
            max_x (int): The maximum x value.
            max_y (int): The maximum y value.
        """
        x = (self._position.get_x() + self._velocity.get_x()) % max_x
        #set to fixed number
        y = (self._position.get_y() + self._velocity.get_y()) % max_y
        self._position = Point(x, y)

    def set_color(self, color):
        """Updates the color to the given one.
        
        Args:
            color (Color): The given color.
        """
        self._color = color

    def set_position(self, position):
        """Updates the position to the given one.
        
        Args:
            position (Point): The given position.
        """
        self._position = position
    
    def set_font_size(self, font_size):
        """Updates the font size to the given one.
        
        Args:
            font_size (int): The given font size.
        """
        self._font_size = font_size
    
    def set_text(self, text):
        """Updates the text to the given value.
        
        Args:
            text (string): The given value.
        """
        self._text = text

    def set_velocity(self, velocity):
        """Updates the velocity to the given one.
        
        Args:
            velocity (Point): The given velocity.
        """
        self._velocity = velocity





        
        
