import json

with open("questions.json", "r") as file:
    questions = json.load(file)

score = 0

for question in questions:
    print(question["question"])
    for option in question["options"]:
        print(option)
    while True:
        choice = input(f"Answer: ").upper()
        if len(choice) == 1 and choice.isalpha():
            break
        else:
            print("Plese input a letter!")
    if choice == question["answer"]:
        print(f"\nCORRECT!\n")
        score += 1
    else:
        print(f"\nINCORRECT!\n")
print(f"Final Score: {score}/{len(questions)}")