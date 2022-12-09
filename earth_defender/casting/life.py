from ..casting.actor import Actor

class Life(Actor):
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