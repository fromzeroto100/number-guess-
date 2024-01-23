import random
import os

def check_answer():
    if user_guess > answer:
        print("Too high!")
    elif user_guess < answer:
        print("Too low!")    
    else:
        print(f"You got it. The answer was {answer}")

easy_level = 10
dif_level = 5
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")        
    if level == easy:
        return easy_level
    else:
        return dif_level    


print("Welcome to the number guess game")
print("Guess a number between 1 and 100")
answer = randint(1, 100)

user_guess = int(input("Input your guess: "))

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')




