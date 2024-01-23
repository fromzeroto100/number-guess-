import random
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


print("Welcome to the number guess game")

easy_game = [1, 2, 3, 4, 5]
hard_game = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

number = int()
def guess(number):
    number = random.randint()
    return

user_guess = int(input("Input your guess: "))


def check_guess():
    if user_guess > guess:
        print("Too high!")
    elif user_guess < guess:
        print("Too low!")    