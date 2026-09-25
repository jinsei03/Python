import random

def create_enemy(name):
    enemy = {
        "Name": name,
        "Health": random.randint(10, 50),
        "Attack": random.randint(5,10),
        "Defense": random.randint(1,25)
    }
    return enemy

def damage(attacker, defender):
    if attacker['Attack'] <= defender["Defense"]:
        dmg = 1
        print(f"{attacker['Name']} attack: {attacker['Attack']}\n{defender['Name']} defense: {defender['Name']}\nDamage: {dmg}\n")
        defender['Health'] -= dmg
    else:
        dmg = attacker['Attack'] - defender['Defense']
        print(f"{attacker['Name']} attack: {attacker['Attack']}\n{defender['Name']} defense: {defender['Name']}\nDamage: {dmg}\n")
        defender['Health'] -= dmg

print("Create your character!")
stat = {
    "Name" : input("Name: "),
    "Health": int(input("Health: ")),
    "Attack": int(input("Attack: ")),
    "Defense": int(input("Defense: "))
}
enemies = []
enemies.append(create_enemy("Goblin"))
enemies.append(create_enemy("Zombie"))
print(f"\nYou ran into a {enemies[0]['Name']} and a {enemies[1]['Name']}!")


opp = input("Which one are you fighting?: ")
if opp == enemies[0]['Name']:
    print(f"You have chosen to fight the {enemies[0]['Name']}!")
    opp = enemies[0]
elif opp == enemies[1]['Name']:
    print(f"You have chosen to fight the {enemies[1]['Name']}!")
    opp = enemies[1]

while stat['Health'] > 0 and opp['Health'] > 0: 
    damage(stat, opp)
    if opp["Health"] < 0:
        break
    else:
        damage(opp, stat)

if stat["Health"] != 0:
    print(f"{stat['Name']} sucessfully killed the {opp['Name']}")
else:
    print(f"{stat['Name']} was killed by the {opp['Name']}")


    
    
    