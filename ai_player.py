from players import Player
import random

class AiPlayer(Player):
    def __init__(self):
        self.name = "Player 2"
        super().__init__()

    def choose_gesture(self):
        self.chosen_option = random.choice(self.choice)
        return self.chosen_option
