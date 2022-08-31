from players import Player
import random

class AiPlayer(Player):
    def __init__(self):
        #self.name = "Player 2"
        super().__init__()
        self.name = "Player 2"

    def choose_gesture(self):
        bot_selects = random.choice(self.choice)
        #print(f"AI chose {bot_selects}")
        return bot_selects

        # self.chosen_option = random.choice(self.choice)
        # return self.chosen_option
