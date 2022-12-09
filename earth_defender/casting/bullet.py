from .actor import Actor
from constants import *

'''Bullet class performs all things needed to make shoot and track collisions of a bullet'''

class Bullet(Actor):

    def __init__(self):
        super().__init__()  

# Get the bullets list from cast
# Grab a bullet from the bullets list at index self._counter
# Set the color, and position of the bullet
    def create_bullet(self, cast):
        '''Creates bullets and sets their position to the players current position'''
        new_bullet = Bullet()
        new_bullet.set_text("^")
        new_bullet.set_font_size(BULLET_SIZE)
        new_bullet.set_color(WHITE)
        # call player in order to set positon to bullet position
        player = cast.get_first_actor("player")
        new_bullet.set_position(player.get_position())
        # add bullet to cast for use throughout
        cast.add_actor("bullets", new_bullet)

# Move the bullet one space up
    def move_next(self):
        self._position.y -= 8
