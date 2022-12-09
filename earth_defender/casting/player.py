from .actor import Actor
from constants import *
from ..shared.point import Point

class Player(Actor):

    def __init__(self):
        super().__init__()

    def create_player(self, cast):
        player = Player()
        position = Point(450, 575)

        player.set_text("#")
        player.set_font_size(PLAYER_SIZE)
        player.set_color(WHITE)
        player.set_position(position)
        cast.add_actor("player", player)
