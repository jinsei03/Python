import random

words = ["python", "games", "mystery", "code", "work"]

word = random.choice(words)

hidden  = []
guesses = []

print(word)
for i in range(len(word)):
    hidden.append("-")
print(*hidden)

while "-" in hidden:
    guess = input(f"Guess a letter: ")
    while guess in guesses:
        guess = input(f"You already guessed that letter!\n Guess a letter: ")
    for i in range(len(word)):
        if guess == word[i]:
            hidden[i] = word[i]
    guesses.append(guess)
    print(*hidden)

print("\nGood job!")

