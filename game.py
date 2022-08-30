from ai_player import AiPlayer
from human_player import HumanPlayer

class Game:
    def __init__(self):
        self.user_1 = HumanPlayer("Player 1")
        self.user_2 = HumanPlayer("Player 2")
        self.bot = AiPlayer()

#In def play_game_human(self), fix self.user_X names
#Max function? Determine winner.

    def run_game(self):
        # self.display_welcome()
        # self.display_rules()
        self.choose_opponent()
        # self.game_options()
        # self.display_winner()
        
    def display_welcome(self):
        print('Wanna play Rock, Paper, Scissors, Lizard, and Spock?')

    def choose_rounds(self):
        options = [3, 5, 7, 9]
        print('''
        1: 3 rounds
        2: 5 round
        3: 7 rounds
        4: 9 rounds
        ''')
        return options[(int(input("Select the amount of rounds you'd like: ")))-1] # add input subtraction like choosing gesture
    
    def choose_opponent(self):
        x = int(input('''Choose your opponent: AI (Computer) or Multiplayer (another Human)
        1: Ai
        2: Multiplayer
        '''))
        if x == 1:
            self.play_game_ai()
        if x == 2:
            self.play_game_human()
        else:
            self.choose_opponent()

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


    def play_game_ai(self): #might need add parenthesis 
        number_of_rounds = self.choose_rounds()
        current_round = 1
        while current_round < number_of_rounds:
            self.user_1.chosen_option = self.user_1.choose_gesture()
            self.bot.choice = self.bot.choose_gesture()        #     
            if self.user_1.chosen_option == self.user_1.choice[2] and (self.bot.choice == self.bot.choice[4] or self.bot.choice[0]): 
                self.user_1.points_earned += 1

            elif self.user_1.chosen_option == self.user_1.choice[4] and (self.bot.choice == self.bot.choice[3] or self.bot.choice[0]): 
                self.user_1.points_earned += 1 

            elif self.user_1.chosen_option == self.user_1.choice[3] and (self.bot.choice == self.bot.choice[2] or self.bot.choice[1]):  
                self.user_1.points_earned += 1 
        
            elif self.user_1.chosen_option == self.user_1.choice[0] and (self.bot.choice == self.bot.choice[1] or self.bot.choice[3]):  
                self.user_1.points_earned += 1 

            elif self.user_1.chosen_option == self.user_1.choice[1] and (self.bot.choice == self.bot.choice[4] or self.bot.choice[2]): 
                self.user_1.points_earned += 1
        
            elif self.user_1.chosen_option == self.bot.choice:
                pass
            else:
                self.bot.points_earned += 1
        self.display_winner()                
                
                        
    def play_game_human(self):
        number_of_rounds = self.choose_rounds()
        current_round = 0
        while current_round <= number_of_rounds:
            print("Player1")#self.user_1.name
            player_one_choice = self.user_1.choose_gesture()
            player_two_choice = self.user_2.choose_gesture()
 #utilize p1 choice as temporary variable           
            
            self.user_1.chosen_option = self.user_1.choose_gesture()
            print("player2")#self.user_2.name
            self.user_2.chosen_option = self.user_2.choose_gesture()
            current_round += 1
            # Player 1 has Lizard and Player 2 has either Scissors or Rock, Player 2 wins
            if player_one_choice == "Lizard" and (player_two_choice == "Rock" or player_two_choice == "Scissors"):
                self.user_2.points_earned += 1
            if self.user_1.chosen_option == self.user_1.choice[2]  and (self.user_2.choice == self.user_2.choice[4] or self.user_2.choice[0]): 
                self.user_2.points_earned += 1
#REFACTOR with dictionaries?
            elif self.user_1.chosen_option == self.user_1.choice[4]  and (self.user_2.choice == self.user_2.choice[3] or self.user_2.choice[0]): 
                self.user_2.points_earned += 1 

            elif self.user_1.chosen_option == self.user_1.choice[3]  and (self.user_2.choice == self.user_2.choice[2] or self.user_2.choice[1]):  
                self.user_1.points_earned += 1 
        
            elif self.user_1.chosen_option == self.user_1.choice[0] and (self.user_2.choice == self.user_2.choice[1] or self.user_2.choice[3]):
                self.user_1.points_earned += 1 

            elif self.user_1.chosen_option == self.user_1.choice[1]  and (self.user_2.choice == self.user_2.choice[4] or self.user_2.choice[2]): 
                self.user_1.points_earned += 1
        
            elif self.user_1.chosen_option == self.user_2.choice:
                pass
            else:
                self.user_2.points_earned += 1
                
        
        self.display_winner()


    def display_winner(self):
        if self.user_1.points_earned >= (number_of_rounds / 2):
            print(f"{self.user_1} wins!")
        elif self.user_2.points_earned >= (number_of_rounds / 2):
            print(f"{self.user_2} wins!")
        elif self.bot.points_earned >= (number_of_rounds / 2):
            print(f"{self.bot} wins!")
        else:
            pass


    # def display_winner(self): #alternate approach to calculate winner
    # while points_earned < (number rounds /2):
    #     winning_points = number_of_rounds/2
    #     if self.user_1.points_earned or self.user_2.points_earned or self.bot.points_earned >= (winning_points) >#end of game 
    #         #MAX function built in
    #         winners_points =  [self.user_1.points_earned, self.user_2.points_earned, self.bot.points_earned]
    #         which is greater than 
    #         #     print(f"{self.user_2} wins!")
    #         # elif :
    #             print(f"{the_winner} wins!")
            
    #         return the_winner[(int(winners_points("the winner is: based on the index ")))-1]
        
            