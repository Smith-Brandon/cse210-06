import random
from turtle import *
from constants import *
from ..casting.message import Message
from ..casting.actor import Actor
from ..shared.color import Color
from ..shared.point import Point
from ..casting.asteroids import Asteroids


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
        self.score_val = 0  # Starting score
        # Number of asteroids on the page (10 was set on main change this if main is modified)
        self.current_asteroids = 10
        self.total_asteroids = 40  # Max number of asteroids on current level
        self.lives_val = 3  # starting number of lives
        self.keep_playing = True  # Used for end game logic
        self.speed = 1  # Speed of asteroids
        self.level = 1  # Starting level
        self.current_level = 1  # Current level

    def start_game(self, cast):
        """Starts the game using the given cast. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.open_window()
        bullets = cast.get_actors("bullets")
        if len(bullets) != 0:
            print(bullets)
            for bullet in bullets:
                cast.remove_actor("bullets", bullet)

        while self._video_service.is_window_open():

            self._get_inputs(cast)
            self._do_updates(cast)
            self._do_outputs(cast)

        self._video_service.close_window()

    def _get_inputs(self, cast):
        """Gets directional input from the keyboard and applies it to the player.
        Also gets the player's bullets and adjusts the level.

        Args:
            cast (Cast): The cast of actors.
        """
        player = cast.get_first_actor("player")
        velocity = self._keyboard_service.get_direction()
        player.set_velocity(velocity)
        bullets = self._keyboard_service.make_bullet(cast)

        level = cast.get_first_actor("level")
        level.set_text('Level ' + str(self.level))

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
        level = cast.get_first_actor("level")

        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        player.move_next(max_x, max_y)

        for bullet in bullets:
            bullet.move_next()
            bullet_position = bullet.get_position()
            bullet_y = bullet_position.get_y()

            if bullet_y <= 0:
                bullet.set_text("")
                cast.remove_actor("bullets", bullet)

        for asteroid in asteroids:
            asteroid.move_next(int(self.speed))
            asteroid_position = asteroid.get_position()
            asteroid_y = asteroid_position.get_y()

            for bullet in bullets:
                bullet_position = bullet.get_position()

                # drop bullets when they leave the screen
                bullet_y = bullet_position.get_y()
                bullet_x = bullet_position.get_x()
                astroid_x = asteroid_position.get_x()

                if bullet_x > astroid_x - 15 and bullet_x < astroid_x + 15:
                    if bullet_y < asteroid_y:

                        cast.remove_actor("bullets", bullet)
                        cast.remove_actor("asteroids", asteroid)
                        if self.keep_playing:
                            self.score_val += 100

            # pop if asteroid reaches end of screen and remove points
            if asteroid_y >= 600:
                cast.remove_actor("asteroids", asteroid)
                # asteroid.set_text("")
                if self.lives_val > 0:
                    self.lives_val = lives.lose_lives(self.lives_val)

        if len(asteroids) <= 0 and self.current_asteroids == self.total_asteroids and self.lives_val > 0:
            self.level = level.level_up()
            self.current_level += 1
            self.total_asteroids = 40 + self.level * 5
            self.current_asteroids = 10
            self.speed *= 1.3
            if self.level % 5 == 0:
                self.lives_val = lives.add_life(self.lives_val)
            self._video_service.close_window()
            self.start_game(cast)

        score.set_text("Score: " + str(self.score_val))
        lives.set_text("Lives: " + str(self.lives_val))

        if self.lives_val <= 0:
            self.keep_playing = False

        self._game_over(cast)

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
        """Creates asteroids and adds them to the cast.

        Args:
            cast (Cast): The cast of actors.
        """
        # Get random number of asteroids to create
        new_asteroids = random.randint(1, 5)
        # Check if new_asteroids is within the levels total_asteroid count
        temp = self.current_asteroids + new_asteroids
        if temp <= self.total_asteroids:  # If within range add to asteroid counter and create objects
            self.current_asteroids += new_asteroids
        else:  # If not get remaining number of asteroids and create that
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
            asteroids = Asteroids()
            position = Point(random.randint(2, 898), 0)
            asteroids.set_text("*")
            asteroids.set_font_size(ASTROIDS_SIZE)
            asteroids.set_color(color)
            asteroids.set_position(position)
            cast.add_actor("asteroids", asteroids)

    def _game_over(self, cast):
        """Ends the game if the player has no lives left.

        Args:
            cast (Cast): The cast of actors.
        """
        # Checks to see that the game has ended
        if self.keep_playing == False:

            # Sets the postion of the game over text
            x = int(900 / 2.3)
            y = int(600 / 2)
            position = Point(x, y)

            # Creates the game over text
            message = Message()
            message.create_message(cast, GAME_OVER_MESSAGE_TEXT, GAME_OVER_MESSAGE_POSITION)
            # Runs through setting the game back up
            if self._keyboard_service.get_play_again():
                self.keep_playing = True
                self.lives_val = 3
                self.score_val = 0
                self.total_asteroids = 40
                self.current_asteroids = 10
                self.speed = 1
                self.level = 1
                self.current_level = 1
                for message in cast.get_actors("messages"):
                    cast.remove_actor("messages", message)
                    message.set_text("")
                for asteroid in cast.get_actors("asteroids"):
                    cast.remove_actor("asteroids", asteroid)
                    asteroid.set_text("")
                for bullet in cast.get_actors("bullets"):
                    cast.remove_actor("bullets", bullet)
                    bullet.set_text("")

                level = cast.get_first_actor("level")
                level.reset_level()

                self._video_service.close_window()
                self.start_game(cast)
