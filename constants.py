import random
from earth_defender.shared.color import Color
from earth_defender.shared.point import Point


"""Main Constants"""
FRAME_RATE = 60
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 8
FONT_SIZE = 15
COLS = 60
ROWS = 40
CAPTION = "Earth Defender"
WHITE = Color(255, 255, 255)
PLAYER_SIZE = 25
ASTROIDS_SIZE = 20
BULLET_SIZE = 30
GAME_OVER_MESSAGE_POSITION = Point(int(900 / 2.3), int(600 / 2))
GAME_OVER_MESSAGE_TEXT = "    GAME OVER!\nPress 'y' to play again!"