# Make a one player Rock-Paper-Scissors game.
# (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner,
# and ask if the players want to start a new game)
# Remember the rules:
# Rock beats scissors
# Scissors beats paper
# Paper beats rock
import random

print("1. NEW GAME")
print("2. RULES")
print("3. QUIT")
player_answer = int(input(": "))

if player_answer == 1:
    print("-" * 50)
    player_one = input("Hello player, whats your name: ")
    player_two = "Computer"
    print("-" *50)

    player_one_win = 0
    player_two_win = 0

    while player_one_win < 3 and player_two_win < 3:
        a = input("{} choose paper/rock or scissors: ".format(player_one)).lower()
        b = random.choice(['rock', 'paper', 'scissors'])

        if (a == "paper" and b == "rock") or (a == "rock" and b == "scissors") or (a == "scissors" and b == "paper"):
            print("{} {} win!".format(player_one, player_one_win + 1))
            player_one_win += 1
        elif (a == "paper" and b == "scissors") or (a == "rock" and b == "paper") or (a == "scissors" and b == "rock"):
            print("{} {} win!".format(player_two, player_two_win + 1))
            player_two_win += 1
        else:
            print("*" * 50)
            print("Try again!")
            print("*" * 50)
            continue

    if player_one_win == 3:
        print("*" * 50)
        print("{} WINNER".format(player_one))
    elif player_two_win == 3:
        print("*" * 50)
        print("{} WINNER".format(player_two))
