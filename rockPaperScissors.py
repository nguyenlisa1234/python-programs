# Homework 6: While Loops
# White Python
# 10/02/2023

import random
import sys

user_input = ""

rounds_played = 0
user_wins = 0
user_losses = 0
tie_games = 0

while True:
    while user_input != 1 and user_input != 2 and user_input != 3 and user_input != 0:
        user_input = int(input("Choose: Rock (1), Paper (2), Scissors (3), or Quit (0): "))
        if user_input == 0:
            sys.exit()
        elif user_input == 1 and user_input == 2 and user_input == 3:
            break
        else:
            print(user_input)

        computer_input = random.randint(1,3)

        if user_input == 1:
            user_output = "rock"
        elif user_input == 2:
            user_output = "paper"
        elif user_input == 3:
            user_output = "scissors"

        if computer_input == 1:
            computer_outcome = "rock"
        elif computer_input == 2:
            computer_outcome = "paper"
        elif computer_input == 3:
            computer_outcome = "scissors"

        if user_input == computer_input:
            print(f"Tie game fellas, user inputed {user_output} and computer inputed {computer_outcome}.")
            tie_games += 1
        elif user_input == 1:
            if computer_input == 2:
                print(f"Daaaaang, can't even win in Rock, Paper, Scissors... user inputed {user_output} and computer inputed {computer_outcome}.")
                user_losses += 1
            else:
                print(f"Woooooh a win is a win my friend! User inputed {user_output} and computer inputed {computer_outcome}.")
                user_wins += 1
        elif user_input == 2:
            if computer_input == 3:
                print(f"Daaaaang, can't even win in Rock, Paper, Scissors... user inputed {user_output} and computer inputed {computer_outcome}.")
                user_losses += 1
            else:
                print(f"Woooooh a win is a win my friend! User inputed {user_output} and computer inputed {computer_outcome}.")
                user_wins += 1
        elif user_input == 3:
            if computer_input == 1:
                print(f"Daaaaang, can't even win in Rock, Paper, Scissors... user inputed {user_output} and computer inputed {computer_outcome}.")
                user_losses += 1
            elif user_input == 3 and computer_input == 2:
                print(f"Woooooh a win is a win my friend! User inputed {user_output} and computer inputed {computer_outcome}.")
                user_wins += 1

        rounds_played += 1

        print(f"Round {rounds_played}")
        print(f"User wins: {user_wins}")
        print(f"User_losses: {user_losses}")
        print(f"Tie games: {tie_games}")

        print("Starting next round... ")
    user_input = ""