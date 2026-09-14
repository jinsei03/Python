import random

words = ["python", "games", "mystery", "code", "work"]

word = random.choice(words)

hidden  = []
guesses = []
lives = 6

for i in range(len(word)):
    hidden.append("-")
print(*hidden)

while "-" in hidden and lives != 0:
    while True:
        guess = input(f"\nGuess a letter: ")
        while guess in guesses:
            guess = input(f"You already guessed that letter!\nGuess a letter: ")
        if len(guess) == 1 and guess.isalpha():
            break
        print("Please only enter one letter: ")
    for i in range(len(word)):
        if guess == word[i]:
            hidden[i] = word[i]
    if guess not in word:
        print(f"Wrong guess")
        lives -= 1
        print(f"You have {lives} lives!")
    guesses.append(guess)
    print(*hidden)

if lives == 0:
    print(f"Nice try!\nThe word was {word}")
else:
    print("Good job!")

