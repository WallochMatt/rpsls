# Rock Paper Scissors Lizard Spock

A terminal game of RPSLS from the CBS sitcom 'The Big Bang Theory'.
Within this project, you can play a game of RPSLS against the code itself, or another person (assuming they are with you in person).
As for how the game is played, I think Sheldon explains it best: https://www.youtube.com/watch?v=Z2Dwxv-EMTM

## Built With

![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)


## My Process

This project was worked on over the course of 3 days. It was the first experience for a paired programming approach. My partner, [Michael J. Thompson](https://github.com/the1michaelt) and I, switched between "Driver" and "Navigator" each work day. We first needed to familiarize ourselves with the game's unique rules. With playing through testing matches, we also had a good opportunity to make alterations to our UI/UX within the console.


## Technical Showcase

There was one point in this project where we were having issues determining how to instantiate the opponent after the user has chosen to play either Single Player or Multiplayer. Originally, we had a long section of sequential only code to run all the logic. As it changed into methods, we ended up writing a method that would ask the user to choose and return the object of either a second HumanPlayer or an AiPlayer. This method was called from the assignment of the second player. Capturing the return on the instance variable of our Game for user_2. Here is what I am referring to:

        class Game:
            def __init__(self):
                self.user_1 = HumanPlayer("Player 1")
                self.user_2 = self.choose_opponent()


            def choose_opponent(self):
                who_you_chose = int(input('''Choose your opponent: AI (Computer) or Multiplayer (another Human)
                1: Ai
                2: Multiplayer
                '''))
                if who_you_chose == 1:
                    return AiPlayer()

                elif who_you_chose == 2:
                    return HumanPlayer("Player 2")

                else:
                    self.choose_opponent()


## Installation Steps

1) Download the .zip file from this repository
2) Open the unzipped file in your preferred IDE, I used VSCode
3) Select the main.py file, it can only run through main.py!
4) Open a new terminal (top left toolbar in VSCode)
5) Hit Run Python File (Top right in VSCode)
6) At this point, you have started the game, and the UI within the console should be able to get you through playing your first match!


## Continued Development

After completing this project I was really interested in further dives into Object Oriented Programming. I had also walked away with a much better understanding of utilizing methods/functions. Since this project's end, I have actually recreated it in Java. Check that out [here!](https://github.com/WallochMatt/RPSLS-in-Java) This rendition actually had an interesting tid-bit. While recreating the methods, I used the same logic. However, the section for determining a winner was different between the two languages. In Python, the math would be exact. So 3 / 2 would be 1.5. However, as I had assigned those numbers as Int in Java, it was actually rounding down to the nearest whole number. Which was an interesting thing to discover during the debugging detective work.


## Contact Me 

See more of my repositories [here!](https://github.com/WallochMatt?tab=repositories)

Message me on [LinkedIn!](https://www.linkedin.com/in/matthew-walloch-931409250/)

Or shoot me an email!: matthewrwalloch@gmail.com


# User Stories
For the technical people who are curious about the User Stories/Goals of this project, here they are:


    A terminal game for playing Rock, Paper, Scissor,  Lizard, Spock

    As a developer, I want to make at least 10 commits with descriptive messages.

    As a developer, I want to find a way to properly incorporate inheritance into my game.

    As a developer, I want to account for and handle bad user input, ensuring that any user input is validated and reobtained if necessary.

    As a developer, I want to store all of the gesture options/choices in a List (AS STRINGS). I want to find a way to utilize the list of gestures within my code (display gesture options, assign player a gesture, etc).

    As a player, I want the correct player to win a given round based on the choices made by each player.  See below for game rules!

    As a player, I want the game of RPSLS to be at minimum a “best of three” to decide a winner. 

    As a player, I want the option of a single player (human vs AI) or a multiplayer (human vs human) game.
