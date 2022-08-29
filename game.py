from ai_player import AiPlayer
from human_player import HumanPlayer

class Game:
    def __init__(self):
        self.user_1 = HumanPlayer("Player 1")
        self.user_2 = HumanPlayer("Player 2")
        self.bot = AiPlayer()

    def run_game(self):
        self.display_welcome()
        self.display_rules()
        #choose ai or human
        self.play_game()
        self.display_winner()
        
    def display_welcome(self):
        print('Wanna play Rock, Paper, Scissors, Lizard, and Spock?')

    def choose_rounds(self):
        options = [3, 5, 7, 9]
        print('''1: 3 rounds
        2: 5 round
        3: 7 rounds
        4: 9 rounds
        ''')
        int(input("Select the amount of rounds you'd like: ") - 1) # add inpu subtraction like choosing gesture

    def choose_opponent(self):
        x = int(input('''Ai vs Multiplayer
        1: Ai
        2: Multiplayer
        '''))
        if x == 1:
            pass #play ai game method
        if x == 2:
            pass #mp method
        


    def display_rules(self):
        print(f'''Remember the rules: 
Scissors cuts Paper
Paper covers Rock
Rock crushes Lizard
Lizard poisons Spock
Spock smashes Scissors
Scissors decapitates Lizard
Lizard eats Paper
Paper disproves Spock
Spock vaporizes Rock
Rock crushes Scissors

Ready to play?''')


    def play_game_ai(self): #might need add paranthesis 
        current_round = 1
        while current_round < number_of_rounds:

            if self.user_1.choice == self.user_1.choice[2]  and self.bot.choice == self.bot.choice[4] or self.bot.choice[0]: 
                self.user_1.points_earned += 1

            elif self.user_1.choice == self.user_1.choice[4]  and self.bot.choice == self.bot.choice[3] or self.bot.choice[0]: 
                self.user_1.points_earned += 1 

            elif self.user_1.choice == self.user_1.choice[3]  and self.bot.choice == self.bot.choice[2] or self.bot.choice[1] :  
                self.user_1.points_earneds += 1 
        
            elif self.user_1.choice == self.user_1.choice[0]  and self.bot.choice == self.bot.choice[1] or self.bot.choice[3] :  
                self.user_1.points_earned += 1 
        

            elif self.user_1.choice == self.user_1.choice[1]  and self.bot.choice == self.bot.choice[4] or self.bot.choice[2]: 
                self.user_1.points_earned += 1
        
            elif self.user_1.choice == self.bot.choice:
                pass
            
            else: 
                pass#player 2  += 1
    
    def play_game_human(self):
        pass

    def display_winner(self):
        pass
    #if win_round >= (rounds%2+1)  #modulo? Not // which returns whole number?
        #logic
        #print({winning_player}, wins!'')

