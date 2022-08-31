
from ai_player import AiPlayer
from human_player import HumanPlayer

class Game:
    def __init__(self):
        self.user_1 = HumanPlayer("Player 1")
        self.user_2 = HumanPlayer("Player 2")
        self.bot = AiPlayer()

#Max function? Determine winner.

    def run_game(self):
        #print(self.user_1.name)
        self.display_welcome()
        self.display_rules()
        self.choose_opponent()
        #play again ? choose opp


    def display_welcome(self):
        print('Wanna play Rock, Paper, Scissors, Lizard, and Spock?')

    def choose_rounds(self):
        options = [3, 5, 7, 9] 
       
        selected_option = options[(int(input('''Choose the amount of rounds: 
        1: 3 rounds
        2: 5 round
        3: 7 rounds
        4: 9 rounds
        '''))) - 1]
    
        if options == 0 or 1 or 2 or 3: #
            return selected_option
        else:
            self.choose_rounds()


    def choose_opponent(self):
        who_you_chose = int(input('''Choose your opponent: AI (Computer) or Multiplayer (another Human)
        1: Ai
        2: Multiplayer
        '''))
        if who_you_chose == 1:
            self.play_game_ai()

        elif who_you_chose == 2:
            self.play_game_human()

        else:
            self.choose_opponent()#works with integers but not letters

    def display_rules(self):
        print('''Remember the rules: 
Scissors cuts Paper, Scissors decapitates Lizard
Paper covers Rock, Paper disproves Spock
Rock crushes Lizard, Rock crushes Scissors
Lizard poisons Spock, Lizard eats Paper
Spock smashes Scissors, Spock vaporizes Rock

Ready to play?''')

    def round_for_user(self):
        self.user_1.points_earned += 1
        print(f"{self.user_1.name} won the round and has {self.user_1.points_earned} points total.")

    def play_game_ai(self):
        number_of_rounds = self.choose_rounds()
        current_round = 0
        while current_round < number_of_rounds:
            current_round += 1
            print(f'''Round {current_round}:
{self.user_1.name} choose gesture: ''')

            player_one_choice = self.user_1.choose_gesture()
            print(f"{self.bot.name} choose gesture:")
            bot_choice = self.bot.choose_gesture()

            if player_one_choice== "Lizard" and (bot_choice== "Spock" or bot_choice == "Paper"):
                self.round_for_user()

            elif player_one_choice== "Rock" and (bot_choice== "Scissors" or bot_choice== "Lizard"): 
                self.round_for_user()

            elif player_one_choice== "Scissors" and (bot_choice== "Paper" or bot_choice== "Lizard"):  
                self.round_for_user()
        
            elif player_one_choice== "Spock" and (bot_choice== "Scissors" or bot_choice== "Rock"):  
                self.round_for_user()

            elif player_one_choice== "Paper" and (bot_choice== "Rock" or bot_choice== "Spock"): 
                self.round_for_user()

            elif player_one_choice== bot_choice:
                current_round -= 1
                print("Tie. Replaying the round")

            else:
                self.bot.points_earned += 1
                print(f"The AI won the round and has {self.bot.points_earned} points total.")

            # print(f"{self.user_1.name} chose {self.user_1.choice}")
            # print(f"{self.bot.name} chose {self.bot.choice}")
            current_round = self.display_winner(number_of_rounds, current_round)                
                
                        
    def play_game_human(self):
        number_of_rounds = self.choose_rounds()
        current_round = 0
        while current_round < number_of_rounds:         
            current_round += 1
            print(f'''Round {current_round}:
{self.user_1.name} choose gesture: ''')

            player_one_choice = self.user_1.choose_gesture()
            print(f"{self.user_2.name} choose gesture:")
            user_2_choice = self.user_2.choose_gesture()

            if player_one_choice== "Lizard" and (user_2_choice== "Spock" or user_2_choice == "Paper"):
                self.round_for_user()

            elif player_one_choice== "Rock" and (user_2_choice== "Scissors" or user_2_choice== "Lizard"): 
                self.round_for_user()

            elif player_one_choice== "Scissors" and (user_2_choice == "Paper" or user_2_choice == "Lizard"):  
                self.round_for_user()
        
            elif player_one_choice== "Spock" and (user_2_choice== "Scissors" or user_2_choice== "Rock"):  
                self.round_for_user()

            elif player_one_choice== "Paper" and (user_2_choice== "Rock" or user_2_choice== "Spock"): 
                self.round_for_user()

            elif player_one_choice== user_2_choice:
                current_round -= 1
                print("Tie. Replaying the round")

            else:
                self.user_2.points_earned += 1
                print(f"{self.user_2.name} won the round and has {self.user_2.points_earned} points total.")

            # print(f"{self.user_1.name} chose {player_one_choice}") 
            # print(f"{self.user_2.name} chose {user_2_choice}") 
        
            current_round = self.display_winner(number_of_rounds, current_round) 


    def game_over(self):
        print("GAME OVER")
        if self.user_1.points_earned > 0:
            print(f"{self.user_1.name} won {self.user_1.points_earned} rounds")
        if self.user_2.points_earned > 0:
            print(f"{self.user_2.name} won {self.user_2.points_earned} rounds")
        if self.bot.points_earned > 0:
            print(f"{self.bot.name} won {self.bot.points_earned} rounds")

        


    def display_winner(self, number_of_rounds, current_round):
        thatvar = False
        if self.user_1.points_earned >= (number_of_rounds / 2):
            print(f"{self.user_1.name} wins!")
            self.game_over()
            thatvar = True
        
        elif self.user_2.points_earned >= (number_of_rounds / 2):
            print(f"{self.user_2.name} wins!")
            self.game_over()
            thatvar = True

        elif self.bot.points_earned >= (number_of_rounds / 2):
            print(f"{self.bot.name} wins!")
            self.game_over()
            thatvar = True
           
        if thatvar == True:
            current_round = number_of_rounds
            return current_round
        else:
            current_round = current_round
            return current_round
        


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
        
    # def gameplay_loop_pvp(self):
    #     player_one_choice = self.user_1.choose_gesture()
    #     print(f"{self.user_2.name} choose gesture:")
    #     player_two_choice = self.user_2.choose_gesture()
    #     if player_one_choice== "Lizard" and (player_two_choice== "Spock" or player_two_choice == "Paper"):
    #         self.round_for_user()

    #     elif player_one_choice== "Rock" and (player_two_choice== "Scissors" or player_two_choice== "Lizard"): 
    #         self.round_for_user()

    #     elif player_one_choice== "Scissors" and (player_two_choice== "Paper" or player_two_choice== "Lizard"):  
    #         self.round_for_user()
            
    #     elif player_one_choice== "Spock" and (player_two_choice== "Scissors" or player_two_choice== "Rock"):  
    #         self.round_for_user()

    #     elif player_one_choice== "Paper" and (player_two_choice== "Rock" or player_two_choice== "Spock"): 
    #         self.round_for_user()
            
    #     elif player_one_choice== player_two_choice:
    #         current_round -= 1
    #         print("Tie. Replaying the round")

    #     else:
    #         self.bot.points_earned += 1
    #         print(f"{self.user_2.name} won the round and has {self.user_2.points_earned} points total.")


    # def gameplay_loop_ai(self):
    #     player_one_choice = self.user_1.choose_gesture()
    #     bot_choice = self.bot.choose_gesture()
    #     print(f"{self.bot.name} choose gesture:")

    #     if player_one_choice== "Lizard" and (bot_choice== "Spock" or bot_choice == "Paper"):
    #         self.round_for_user()

    #     elif player_one_choice== "Rock" and (bot_choice== "Scissors" or bot_choice== "Lizard"): 
    #         self.round_for_user()

    #     elif player_one_choice== "Scissors" and (bot_choice== "Paper" or bot_choice== "Lizard"):  
    #         self.round_for_user()
        
    #     elif player_one_choice== "Spock" and (bot_choice== "Scissors" or bot_choice== "Rock"):  
    #         self.round_for_user()

    #     elif player_one_choice== "Paper" and (bot_choice== "Rock" or bot_choice== "Spock"): 
    #         self.round_for_user()

    #     elif player_one_choice== bot_choice:
    #         current_round -= 1 #return this 
    #         print("Tie. Replaying the round")

    #     else:
    #         self.bot.points_earned += 1
    #         print(f"The AI won the round and has {self.bot.points_earned} points total.")