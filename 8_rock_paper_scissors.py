# Make a one player Rock-Paper-Scissors game.
# (Hint: Ask for player name and plays(using input), compare them, print out a message of congratulations to the winner)
# Remember the rules:
# Rock beats scissors
# Scissors beats paper
# Paper beats rock
import random


def game():

    beginning = input("\n1. NEW GAME\n2. RULES\n3. QUIT\n: ")

    if beginning == "1":
        print("-" * 50)
        player_one = input("Whats your name?: ")
        player_two = "Computer"

        player_one_win = 0
        player_two_win = 0

        while player_one_win < 3 and player_two_win < 3:
            a = input("{} write 'paper', 'rock' or 'scissors'. \n: ".format(player_one)).lower()
            b = random.choice(['rock', 'paper', 'scissors'])

            if (a == "paper" and b == "rock") or (a == "rock" and b == "scissors") or (a == "scissors" and b == "paper"):
                print("{} {} win!".format(player_one, player_one_win + 1))
                player_one_win += 1
            elif (a == "paper" and b == "scissors") or (a == "rock" and b == "paper") or (a == "scissors" and b == "rock"):
                print("{} {} win!".format(player_two, player_two_win + 1))
                player_two_win += 1
            elif a == b:
                print("Tie!")
            else:
                print("Something went wrong, try again!")
                continue

        if player_one_win == 3:
            print("{} WINNER".format(player_one))
            quit()
        elif player_two_win == 3:
            print("{} WINNER".format(player_two))
            quit()

    elif beginning == "2":
        print("Rock, Paper, Scissors (aka 'Ro-Sham-Bo', janken, 'Bato, Bato, Pick' and 'Scissors, Paper, Stone') "
              "\nis a simple hand game that is played around the world, with many different names and variations. "
              "\nIt is commonly used as a way of coming to decisions, and in some cases is even played for sport. "
              "\nThe rules require that competing players use one hand to form one of three shapes at an "
              "\nagreed-upon time. The person that plays the strongest “object” is the winner of the game. "
              "\nIt's that easy! Rock Paper Scissors is a simple game that anybody can play and win. "
              "\nThere is no obvious advantage to the stronger, older, more experienced opponent."
              "\n\nHere you will play with COMPUTER, remember to choose paper, rock or scissors. Good LUCK!")
        game()

    elif beginning == "3":
        quit()

    else:
        print("Something went wrong, try again!")
        game()


game()
