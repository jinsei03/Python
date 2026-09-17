import random

def bestOf():
    bestOf = input("Would you like a best of 3, 5, or 7?: ")
    while True:
        try:
            bestOf = int(bestOf)
            while bestOf != 3 and bestOf != 5 and bestOf != 7:
                bestOf = int(input("Only input the numbers 3, 5 or 7!: "))
            break
        except ValueError:
            bestOf = input("Only input the numbers 3, 5 or 7!: ")
    if bestOf == 3:
        goal = 2
    elif bestOf == 5:
        goal = 3
    elif bestOf == 7:
        goal = 4
    return goal, bestOf

options = ["rock", "paper", "scissors"]

win = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}

pScore = 0
cScore = 0

goal, games = bestOf()

while pScore != goal and cScore != goal:
    choice = input("Rock, Paper, or Scissors?: ").lower()
    while choice != options[0] and choice != options[1] and choice != options[2]:
        choice = input("Pleas type only: rock, paper, or scissors!: ").lower()

    computer = random.choice(options)

    print(f"You chose {choice}")
    print(f"Computer chose {computer}")

    if computer == choice:
        print("Draw!")
    elif win[choice] == computer:
        print("You win!")
        pScore += 1
    else:
        print("Computer win!")
        cScore += 1

    print(f"Player: {pScore}\nComputer:{cScore}\n")

    if pScore == goal or cScore == goal:
        print(f"Final scores are:\nPlayer: {pScore}\nComputer:{cScore}\n")
        if pScore > cScore:
            print(f"Player has won the best of {games}!")
        else:
            print(f"Computer has wont the best of {games}!")

        playAgain = input("Play again? [y/n]: ")
        while len(playAgain) != 1 or playAgain != "y" and playAgain != "n" or not playAgain.isalpha():
            playAgain = input("Play again? Input ONLY[y/n]: ")
        if playAgain == "y":
            pScore = 0
            cScore = 0
            goal, games = bestOf()
        else:
            print("Good bye!")


