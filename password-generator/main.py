import random

include = {
    "letters": "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "numbers": "0123456789",
    "special": "!@#$%^&*()-_=+[]{};:,.<>?/"
}

password = include["letters"]
user_pw = ""

length = int(input("How long should your password be?: "))
while length <= 2:
    length = int(input("PLEASE MAKE IT MORE THAN 2!: "))
    
numbers = input("Include numbers?: ")
special = input("Include special characters?: ")

user_pw += random.choice(include["letters"])
length -= 1
if numbers == "y":
    password += include["numbers"]
    user_pw += random.choice(include["numbers"])
    length -= 1
if special == "y":
    password += include["special"]
    user_pw += random.choice(include["special"])
    length -= 1

password = list(password)
for _ in range(length):
    user_pw += random.choice(password)
user_pw = list(user_pw)
random.shuffle(user_pw)

print(f"Your password should be: {"".join(user_pw)}")