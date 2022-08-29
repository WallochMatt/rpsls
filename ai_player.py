from players import Player
import random

class AiPlayer(Player):
    def __init__(self):
        self.name = "Player 2"
        #self.points_earned = 
        super().__init__()

    def choose_gesture(self):
        self.choice = random.choice(self.choice)
        print(self.choice)
