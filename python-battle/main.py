import random

#functions
def goblin_attacks(pHP):
    gDMG = random.randint(5,10)
    pHP = pHP - gDMG
    print(f"The goblin dealt {gDMG}!\n\n")
    if pHP < 0:
        pHP = 0
    return pHP

#variables
pHP = 100
gHP = 60

pDMG = 0

healing = 0

#main
print(f"=== Python Battle ==\n\n")

name = input(f"What is your name: ")
print(f"Welcome, {name}!\n\n")

while pHP > 0 and gHP > 0:
    print(f"{name} HP: {pHP}\nGoblin HP: {gHP}\n\nWhat do you want to do?\n1. Attack\n2. Heal\n3. Run\n\n")
    action = input("Choose an action: ")

    while action != "1" and action != "2" and action != "3":
        action = input(f"PLEASE PRESS 1, 2 OR 3 ONLY!!!\nChoose an action: ")

    if action == "1":
        pDMG = random.randint(5,15)
        gHP = gHP - pDMG
        print(f"\nYou dealt {pDMG} damage!")

        if gHP <= 0:
            gHP = 0
            print(f"You deafeated the Goblin!\n\n")
        else:
            pHP = goblin_attacks(pHP)

    elif action == "2":
        healing = random.randint(10,20)
        pHP = healing + pHP

        if pHP > 100:
            pHP = 100
        print(f"You healed for {healing} HP!\n{name} HP: {pHP}\n")

        pHP = goblin_attacks(pHP)

    elif action == "3":
        print(f"You run away!\n{name} HP: {pHP}\nGoblin HP: {gHP}\n\n")
        break

if pHP == 0:
    print(f"You died!\n{name} HP: {pHP}\nGoblin HP: {gHP}\n\n")
