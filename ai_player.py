from players import Player
import random

class AiPlayer(Player):
    def __init__(self):
        #self.name = "Player 2"
        super().__init__()
        self.name = "Player 2"

    def choose_gesture(self):
        bot_choice = random.choice(self.choice)
        print(f"AI chose {bot_choice}")
        return bot_choice

        # self.chosen_option = random.choice(self.choice)
        # return self.chosen_option
