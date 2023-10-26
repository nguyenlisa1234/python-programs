# Number Guessing Game

import random
import sys

attempts_list = []

def score():
    if not attempts_list:
        print("There is currently no high score. Be the first!")
    else:
        print(f"The current high score is {min(attempts_list)} attempts.")

def game():
    attempts = 0
    rand_num = random.randint(1,10)
    print("Welcome to the Numbers Game!")
    user_name = input("What is your name? ")
    exit_question = input(
        f"Hi, {user_name}, would you like to play "
        f"the guessing game? (Enter Yes/No): ")
    if exit_question.lower() != "yes":
        print("oh... okay... NOT YOU LEAVING ME TOO")
        sys.exit()
    else:
        score()
    while exit_question.lower() == "yes":
        try:
            guess = int(input("Pick a number between 1 and 10: "))
            if guess < 1 or guess > 10:
                raise ValueError(
                    "CAN YOU NOT READ??? 1 TO 10 PEOPLE!")

            attempts += 1
            attempts_list.append(attempts)

            if guess == rand_num:
                print("How the heck did you get that right???")
                print(f'It took you {attempts} attempts.')
                exit_question = input(
                    "Would you like to play again? (Enter Yes/No): ")
                if exit_question.lower() != "yes":
                    print("oh... okay... BYE! I SAID BYE!")
                    break
                else:
                    attempts = 0
                    rand_num = random.randint(1,10)
                    score()
                    continue
            else:
                if guess > rand_num:
                    print("Are you a bird? Cause you are way too high up there.")
                elif guess < rand_num:
                    print("You are as low as a bottomless pit.")

        except ValueError as err:
            print("1 TO 10 PEOPLE! IS IT THAT HARD????")
            print(err)

if __name__ == '__main__':
    game()