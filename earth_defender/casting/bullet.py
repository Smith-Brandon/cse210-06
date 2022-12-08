from .objects import Objects
from constants import *


class Bullet(Objects):
    """Bullet class performs all things needed to make, 
    shoot, and track collisions of a bullet
    """

    def __init__(self):
        """Constructs a new Bullet."""
        super().__init__()

    # Get the bullets list from cast
    # Grab a bullet from the bullets list at index self._counter
    # Set the color, and position of the bullet
    def create_bullet(self, cast):
        """Creates bullets and sets their position equal to the 
        player's current position

        Args:
            cast (Cast): The cast of all actors.
        """
        new_bullet = Bullet()
        new_bullet.set_text("^")
        new_bullet.set_font_size(BULLET_SIZE)
        new_bullet.set_color(WHITE)
        # call player in order to set positon to bullet position
        player = cast.get_first_actor("player")
        new_bullet.set_position(player.get_position())
        # add bullet to cast for use throughout
        cast.add_actor("bullets", new_bullet)

    # def remove_actor(self, group, actor):
    #     """Removes an actor from the given group.
    #     Args:
    #         group (string): The name of the group.
    #         actor (Actor): The actor to remove.
    #     """
    #     if group in self._actors:
    #         self._actors[group].remove(actor)

    # def shoot(self, cast):
    #     bullets = cast.get_actors("bullets")

    #     for bullet in bullets:
    #         position = bullet.get_position()
    #         x = position.get_x()
    #         y = position.get_y()
    #         new_position = Point(x, y - 1)

    #         bullet.set_position(new_position)
