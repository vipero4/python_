# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number,
# then tell them whether they guessed too low, too high, or exactly right.
# (Hint: remember to use the user input lessons from the very first exercise)


# Keep track of how many guesses the user has taken, and when the game ends, print this out.

import random

print("*" *23)
print("*  Lets play a game!  *")
print("* Type: exit for quit *")
print("*" *23)

number = random.choice(range(1, 9))
guess_try = 0

while True:
    guess_number = int(input("Guess the number between 1-9: "))
    guess_try += 1
    if guess_number > 9 or guess_number < 1:
        print("You need to guess number between 1-9. Try again!")
    elif guess_number < number:
        print("Your number is too low. Try again!")
    elif guess_number > number:
        print("Your number is too high. Try again!")
    elif guess_number == number:
        print("Congratulation! The hidden number was ({}). \nYou needed {} attempts.".format(number, guess_try))
        break
