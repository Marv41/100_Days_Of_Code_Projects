import random
import art

TARGET_NUMBER = random.randint(1,100)
print(TARGET_NUMBER)
victory = False

def choose_difficulty(difficulty):
    if difficulty == "easy":
        print("You have 10 attempts remaining to guess the number.")
        return 10
    else:
        print("You have 5 attempts remaining to guess the number.")
        return 5

print(art.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

number_of_attempts = choose_difficulty(input("Choose a difficulty. Type 'easy' or 'hard': "))

while not victory or number_of_attempts == 0:
    guess = int(input("Make a guess: "))
    if guess == TARGET_NUMBER:
        print(f"You got it! The answer was {TARGET_NUMBER}")
        victory = True
    elif guess < TARGET_NUMBER:
        print("Too low")
        print("Guess again.")
        number_of_attempts -= 1
        print(f"You have {number_of_attempts} attempts remaining to guess the number")
    else:
        print("Too high")
        print("Guess again.")
        number_of_attempts -= 1
        print(f"You have {number_of_attempts} attempts remaining to guess the number")

if number_of_attempts == 0:
    print("You've run out of guesses. Refresh the page to run again")


