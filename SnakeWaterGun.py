import random
choices = ['snake', 'water', 'gun']
userPoints = 0
autoPoints = 0 

def showPoints(userPoints, autoPoints):
    print(f"Your points: {userPoints}")
    print(f"My points: {autoPoints}")

print("Welcome to Snake, Water, Gun. You can stop playing with 'exit'. Enter 'show points' to reveal the points.")
print(f"Your points: {userPoints}")
print(f"My points: {autoPoints}")

while True:
    
    userChoice = str(input("Enter your choice: "))
    userChoice = userChoice.lower()
    if userChoice == "exit":
        print("Game quitted.")
        print(f"Your final points: {userPoints}")
        print(f"My final points: {autoPoints}")
        exit()
    if userChoice == "show points":
        showPoints(userPoints, autoPoints)
        continue
    if userChoice not in choices:
        print("Error: Enter valid input.")
        continue
    autoChoice = random.choice(choices)
    if userChoice == autoChoice:
        print(f"My choice was also {autoChoice}")
    else:
        print(f"My choice was {autoChoice}")

    if userChoice == choices[0] and autoChoice == choices[0]:
        print("Draw")
        print(f"Your points: {userPoints}")
        print(f"My points: {autoPoints}")
    elif userChoice == choices[1] and autoChoice == choices[0]:
        autoPoints += 1
        print("You Lose")
        print(f"Your points: {userPoints}")
        print(f"My points: {autoPoints}")
    elif userChoice == choices[2] and autoChoice == choices[0]:
        userPoints += 1
        print("You Won!")
        print(f"Your points: {userPoints}")
        print(f"My points: {autoPoints}")
    elif userChoice == choices[0] and autoChoice == choices[1]:
        userPoints += 1
        print("You Won!")
        print(f"Your points: {userPoints}")
        print(f"My points: {autoPoints}")
    elif userChoice == choices[1] and autoChoice == choices[1]:
        print("Draw")
        print(f"Your points: {userPoints}")
        print(f"My points: {autoPoints}")
    elif userChoice == choices[2] and autoChoice == choices[1]:
        autoPoints += 1
        print("You Lose")
        print(f"Your points: {userPoints}")
        print(f"My points: {autoPoints}")
    elif userChoice == choices[0] and autoChoice == choices[2]:
        autoPoints += 1
        print("You Lose")
        print(f"Your points: {userPoints}")
        print(f"My points: {autoPoints}")
    elif userChoice == choices[1] and autoChoice == choices[2]:
        userPoints += 1
        print("You Won!")
        print(f"Your points: {userPoints}")
        print(f"My points: {autoPoints}")
    elif userChoice == choices[2] and autoChoice == choices[2]:
        print("Draw")
        print(f"Your points: {userPoints}")
        print(f"My points: {autoPoints}")
    else:
        print("Error: Enter valid input.")

    if userPoints >= 5:
        print(f"Game ended. You won with {userPoints-autoPoints}")
    elif autoPoints >= 5:
        print(f"Game ended. I won with {autoPoints-userPoints}")