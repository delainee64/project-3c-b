# Author: Delainee Lenss
# GitHub username: delainee64
# Date: 10/09/2022
# Description: Write a program that prompts the user for an integer that the player will try to guess.
# If the player's guess is higher than the target integer, the program should display "too high"
# If the user's guess is lower than the target integer, the program should display "too low"
# Then the program should print how many guesses it took.

user = int(input("Enter the integer for the player to guess."))
guess = int(input("Enter your guess."))
num = 0

while (True):               # while loop will continue until the guess is correct.
    num = num + 1           # num will count the number of attempts.
    if (guess < user):
        guess = int(input("Too low - try again:"))
    elif (guess > user):
        guess = int(input('Too high - try again:'))
    else:
        break               # break will exit the cycle

print('You guessed it in', num, 'tries.')