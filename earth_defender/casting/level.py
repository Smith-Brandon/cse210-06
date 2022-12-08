from ..casting.actor import Actor

# Add game reset/next level (method in director)
# - reset game when astroids are gone
# - keep track of level
# - increase fall frequency


class Level(Actor):
    '''The level is an integer that controls the speed
    at which the astroids fall to earth. It also controls
    the number of astroids that will fall to earth in order
    to advance to the next level.
    '''

    def __init__(self):
        super().__init__()
        self._level = 1
        self._speed = 1

    def level_up(self):
        self._level += 1
        
        return self._level
        