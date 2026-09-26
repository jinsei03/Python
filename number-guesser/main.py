import random

number = random.randint(1,100)
attempts = 0

while True:
    guess = int(input("Guess the number between 1-100: "))
    if guess > number:
        print("Your guess is too high!")
        attempts += 1
    elif guess < number:
        print("Your guess is too low!")
        attempts += 1
    elif guess == number:
        attempts += 1
        print(f"You correctly guessed the number {number} after {attempts} attempt(s)!")
        replay = input("Would you like to play again? [y/n]: ")
        if replay == "y":
            number = random.randint(1,100)
            attempts = 0
        elif replay == "n":
            break
print("Goodbye!")
