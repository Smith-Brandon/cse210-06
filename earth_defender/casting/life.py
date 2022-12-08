from ..casting.actor import Actor


class Life(Actor):
    """A life is an interger that acts as a counter 
    for the maximum amount of astroids that can fall 
    to earth in one game before causing a game over.

    Every game the player will start with 3 lives 
    and gain 1 life every 5th level.
    """

    def __init__(self):
        """Constructor for the Life class."""
        super().__init__()
        self.level_add_life = 5

    def lose_lives(self, current_lives):
        """Gets the current amount of lives and subtracts 1 life.

        Args:
            current_lives (int): The current amount of lives.
        Returns:
            int: The current amount of lives.
        """

        current_lives -= 1

        return current_lives

    def add_life(self, level, current_lives):
        """Gets the current level and adds a life every 5th level.

        Args:
            level (int): The current level.
            current_lives (int): The current amount of lives.
        Returns:
            int: The current amount of lives.
        """

        if level == self.level_add_life:
            current_lives += 1
            self.level_add_life += 5

        return current_lives
