from ..casting.actor import Actor

class Life(Actor):
    '''A life is an interger that acts as a counter for the maximum amount of astroids that can fall to earth in one game.
    Every game the player will start with 3 lives and gain 1 every 5th level.'''
    def __init__(self):
        self.level_add_life = 5
        self.lives = 0

    '''This method will return lives upon calling to be used with in the game.'''
    def lose_lives(self, current_lives):
        
        current_lives -= 1

        return current_lives
        
 
    '''Method adds a life every 5 levels to the current amount of lives.'''
    def add_life(self, current_lives):

        # if level == self.level_add_life:
        #     current_lives += 1
        #     self.level_add_life += 5
        current_lives += 1

        return current_lives