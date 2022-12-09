from .actor import Actor

class Asteroids(Actor):

    def __init__(self):
        super().__init__()

    def asteroid_bullet(self):
        return self._point

    def get_item_type(self):
        return self._object

    def move_next(self, speed):
        if self._move_counter < 2:
            self._move_counter += 1
        else:
            self._position.y += speed
            self._move_counter = 0
