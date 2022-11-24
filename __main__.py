import os
import random
from tkinter.tix import ROW
from turtle import *


from greed.casting.actor import Actor
from greed.casting.objects import Objects
from greed.casting.cast import Cast

from greed.directing.director import Director

from greed.services.keyboard_service import KeyboardService
from greed.services.video_service import VideoService

from greed.shared.color import Color
from greed.shared.point import Point




FRAME_RATE = 60
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
FONT_SIZE = 15
COLS = 60
ROWS = 40
CAPTION = "Greed"
WHITE = Color(255, 255, 255)
DEFAULT_ARTIFACTS = random.randint(9, 15)



def main():
    
    # create the cast
    cast = Cast()
    
    # create the score
    x = int(MAX_X / 2)
    y = int(MAX_Y / 2)
    position = Point(5, 5)
    score = Objects()
    score.set_text("Player Score: ")
    score.set_font_size(FONT_SIZE)
    score.set_color(WHITE)
    score.set_position(position)
    cast.add_actor("score", score)
    
    # create the player
    x = int(MAX_X / 2)
    y = int(MAX_Y / 2)
    position = Point(450, 575)

    player = Objects()
    player.set_text("#")
    player.set_font_size(FONT_SIZE)
    player.set_color(WHITE)
    player.set_position(position)
    cast.add_actor("player", player)
    
   
    
    for n in range(40):

        x = random.randint(1, COLS - 1)
        y = random.randint(1, ROWS - 1)
        position = Point(x, y)
        position = position.scale(CELL_SIZE)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)

        # create the Gems
        gems = Objects()
        #position = Point(random.randint(2,898), 0)
        gems.set_text("*")
        gems.set_font_size(FONT_SIZE)
        gems.set_color(color)
        gems.set_position(position)
        cast.add_actor("gems", gems)

        x = random.randint(1, COLS - 1)
        y = random.randint(1, ROWS - 1)
        position = Point(x, y)
        position = position.scale(CELL_SIZE)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)

        # create the Rocks
        stones = Objects()
        #position = Point(random.randint(2,898), 0)
        stones.set_text("o")
        stones.set_color(color)
        stones.set_font_size(FONT_SIZE)
        stones.set_position(position)
        cast.add_actor("stones", stones)
    
    # start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(cast)


if __name__ == "__main__":
    main()