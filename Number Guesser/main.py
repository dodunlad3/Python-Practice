#import random module
import random

from random import randint

number = random.randint(1, 100)


guess = int()
lives = 7

print("Welcome to the Python Practice\n")
print("You have 7 lives")


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

if lives == 0:
    print("You lost")

print("The number was " + str(number))