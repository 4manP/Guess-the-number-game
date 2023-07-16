import random

def guess_the_number():
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        guess = input("Guess the number (between 1 and 100), or enter 'q' to quit: ")

        if guess.lower() == 'q':
            print(f"Quitting the game with {attempts} attempts")
            break
        

        guess = int(guess)
        attempts += 1

        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print("Congratulations! You guessed the correct number.")
            print(f"Attempts: {attempts}")
            break

guess_the_number()
