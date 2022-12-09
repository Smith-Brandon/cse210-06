from .actor import Actor

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

    def create_message(self, cast, text, position):
        '''Creates message and sets their position and text to the given parameters.
        
        Args:
            cast (Cast): The cast of all actors
            text (string): The text to display
            position (the position of the message)
        '''
        message = Message()
        # Sets the postion of the game over text
        message.set_text(text)
        message.set_position(position)
        cast.add_actor("messages", message)
        