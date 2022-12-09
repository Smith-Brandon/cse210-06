from .actor import Actor
from constants import *
from ..shared.point import Point


class Message(Actor):

    def __init__(self):
        super().__init__()

    def create_message(self, cast):
        message = Message()
        # Sets the postion of the game over text
        x = int(900 / 2.3)
        y = int(600 / 2)
        position = Point(x, y) 
        message.set_text("    GAME OVER!\nPress 'y' to play again!")
        message.set_position(position)
        cast.add_actor("messages", message)
        