import os
import random
from tkinter.tix import ROW
from turtle import *


from constants import *
from earth_defender.casting.actor import Actor
from earth_defender.casting.objects import Objects
from earth_defender.casting.cast import Cast
from earth_defender.casting.life import Life
from earth_defender.casting.bullet import Bullet

from earth_defender.directing.director import Director

from earth_defender.services.keyboard_service import KeyboardService
from earth_defender.services.video_service import VideoService

from earth_defender.shared.color import Color
from earth_defender.shared.point import Point


def main():

    # create the cast
    cast = Cast()

    # create the score
    position = Point(5, 5)
    score = Objects()
    score.set_text("Player Score: ")
    score.set_font_size(FONT_SIZE)
    score.set_color(WHITE)
    score.set_position(position)
    cast.add_actor("score", score)

    # create the player
    position = Point(450, 575)

    player = Objects()
    player.set_text("#")
    player.set_font_size(PLAYER_SIZE)
    player.set_color(WHITE)
    player.set_position(position)
    cast.add_actor("player", player)

    # create lives
    x = int(MAX_X / 2)
    y = int(MAX_Y / 2)
    position = Point(830, 5)
    lives = Life()
    lives.set_text("Lives: ")
    lives.set_font_size(FONT_SIZE)
    lives.set_color(WHITE)
    lives.set_position(position)
    cast.add_actor("lives", lives)

    for n in range(10):

        x = random.randint(1, COLS - 1)
        #y = random.randint(1, ROWS - 1)
        y = random.randint(1, 20)  # Start at half page
        position = Point(x, y)
        position = position.scale(CELL_SIZE)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)

        # create the asteroids
        asteroids = Objects()
        #position = Point(random.randint(2,898), 0)
        asteroids.set_text("*")
        asteroids.set_font_size(ASTROIDS_SIZE)
        asteroids.set_color(color)
        asteroids.set_position(position)
        cast.add_actor("asteroids", asteroids)

        # Creation of bullet objects with text '^'
        # Position and color not set yet
    # for i in range(50):
    #     bullets = Bullet()
    #     bullets.set_text("^")
    #     bullets.set_font_size(BULLET_SIZE)
    #     cast.add_actor("bullets", bullets)

    # start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service)
    keyboard_service.add_player(cast, player)
    director.start_game(cast)


if __name__ == "__main__":
    main()
