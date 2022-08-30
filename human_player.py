from players import Player

class HumanPlayer(Player):
    def __init__(self, name): #in game.py 
        self.name = name
        super().__init__()

    def choose_gesture(self):
        return self.choice[(int(input("CHOOSE 1-5"))) - 1]
        # self.choice= self.choice[(int(input(f'''Choose your gesture, 1-5:
        #player_one_choice  #utilize p1 choice as temporary variable
        # 1: {self.choice[0]}
        # 2: {self.choice[1]}
        # 3: {self.choice[2]}
        # 4: {self.choice[3]}
        # 5: {self.choice[4]}
        # ''')))-1]
        
        #distinguish between player 1 and 2?
        
        # return self.choice  