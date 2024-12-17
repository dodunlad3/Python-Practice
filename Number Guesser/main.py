#import random module
import random

from random import randint

# Generate a random number between 1 and 100
number = random.randint(1, 100)
# Set the number of lives
lives = 7

print("Welcome to the Python Practice\n")
print("You have 7 lives")

# Ask the user to guess the number
# If the guess is higher than the number, tell the user "Too high"
# If the guess is lower than the number, tell the user "Too low"
# If the guess is correct, tell the user "You got it"
while lives > 0:
    guess = int(input("Guess a number: "))
    if guess == number:
        print("You got it")
        break
    elif guess > number:
        lives -= 1
        print("Too high, try again")
    else:
        lives -= 1
        print("Too low, try again")
    print("You have " + str(lives) + " lives")

# If the user runs out of lives, tell them "You lost"
if lives == 0:
    print("You lost")

print("The number was " + str(number))