from players import Player

class HumanPlayer(Player):
    def __init__(self, name): #in game.py 
        self.name = name
        super().__init__()

    def choose_gesture(self):
        self.choice = self.choice[int(input("CHOOSE 1-5")) - 1]
        print(self.choice) 