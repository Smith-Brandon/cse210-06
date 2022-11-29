from ast import parse
import os
import random
from tkinter.tix import ROW
from turtle import *

from greed.casting.actor import Actor
from greed.shared.color import Color
from greed.shared.point import Point
from ..casting.objects import Objects
from ..casting.life import Life

class Director:
    """A person who directs the game. 

    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _keyboard_service (KeyboardService): For getting directional input.
        _video_service (VideoService): For providing video output.
    """

    def __init__(self, keyboard_service, video_service):
        """Constructs a new Director using the specified keyboard and video services.

        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
            video_service (VideoService): An instance of VideoService.
        """
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        self.moved = 0
        self.score_val = 500
        self.current_asteroids = 10 # Number of asteroids on the page (10 was set on main change this if main is modified)
        self.total_asteroids = 40 # Max number of asteroids on current level
        self.lives_val = 3 #starting number of lives
        self.keep_playing = True #Used for end game logic

    def start_game(self, cast):
        """Starts the game using the given cast. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.open_window()
        while self._video_service.is_window_open():
                self._get_inputs(cast)
                self._do_updates(cast)
                self._do_outputs(cast)
        self._video_service.close_window()

    def _get_inputs(self, cast):
        """Gets directional input from the keyboard and applies it to the player.
        
        Args:
            cast (Cast): The cast of actors.
        """
        player = cast.get_first_actor("player")
        velocity = self._keyboard_service.get_direction()
        player.set_velocity(velocity)        

    def _do_updates(self, cast):
        """Updates the player's position and resolves any collisions with objects.

        Args:
            cast (Cast): The cast of actors.
        """
        score = cast.get_first_actor("score")
        player = cast.get_first_actor("player")
        asteroids = cast.get_actors("asteroids")
        bullets = cast.get_actors("bullets")
        lives = cast.get_first_actor("lives")


        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        player.move_next(max_x, max_y)
                

        for asteroid in asteroids:
            asteroid.fall()
            asteroid_position = asteroid.get_position()
            asteroid_y = asteroid_position.get_y()
            
            # Loop through all bullets 
            for bullet in bullets:
                bullet.move()
                bullet_position = asteroid.get_position()
                bullet_y = bullet_position.get_y()

                # If projectile/bullet hit asteriod
                if bullet_position == asteroid_position:
                    cast.remove_actor(asteroid)
                    cast.remove_actor(bullet)

            # pop if asteroid reaches end of screen and remove points
            if asteroid_y > 590:
                cast.remove_actor(asteroid)
                self.lives_val = lives.lose_lives(self.lives_val)
            
            # if player is hit by asteriod (can't remember if we are keeping this part or not)
            if player._position.equals(asteroid._position):
                self.score_val += 100
                cast.remove_actor(asteroid)
                break
            
        
        score.set_text("Player Score: " + str(self.score_val))
        lives.set_text("Lives: " + str(self.lives_val))

        if self.lives_val == 0:
            self.keep_playing = False

        self._test_game_over(cast)
    
    

        # Create more
        if player._move_counter == 0:
            self.moved += 1
        
        if self.moved == 100:
            self.moved = 0
            # Only create more if current_asteroids is less than level total 
            if self.current_asteroids < self.total_asteroids: 
                self.create_objects(cast)

    def _do_outputs(self, cast):
        """Draws the actors on the screen.

        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.clear_buffer()
        actors = cast.get_all_actors()
        self._video_service.draw_actors(actors)
        self._video_service.flush_buffer()

    def create_objects(self, cast):
        # Get random number of asteroids to create
        new_asteroids = random.randint(1, 5)
        # Check if new_asteroids is within the levels total_asteroid count
        temp = self.current_asteroids + new_asteroids
        if temp <= self.total_asteroids: # If within range add to asteroid counter and create objects
            self.current_asteroids += new_asteroids
        else: # If not get remaining number of asteroids and create that
            new_asteroids = self.total_asteroids - self.current_asteroids
            self.current_asteroids += new_asteroids

        for n in range(new_asteroids):

            x = random.randint(1, 60 - 1)
            y = 0
            position = Point(x, y)
            position = position.scale(15)

            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            color = Color(r, g, b)

            # create the asteroids
            asteroids = Objects()
            position = Point(random.randint(2,898), 0)
            asteroids.set_text("*")
            asteroids.set_font_size(15)
            asteroids.set_color(color)
            asteroids.set_position(position)
            cast.add_actor("asteroids", asteroids)

    def _test_game_over(self, cast):


        if self.keep_playing == False:
            x = int(900 / 2)
            y = int(600 / 2)
            position = Point(x, y)

            message = Actor()
            message.set_text("GAME OVER!")
            message.set_position(position)
            cast.add_actor("messages", message)


