import random

user_wins = 0
computer_wins = 0

options = ["rock","paper","scissors"]

while True:
    user_input = input("Enter rock/paper/scissor or Q to quit.. ").lower()
    if user_input == "q":
        print("You quit.")
        break

    if user_input not in options:
        continue


    randomNum = random.randint(0,2)

    computer_pick = options[randomNum]
    print("Computer picked ",computer_pick+".")

    if user_input == "rock" and computer_pick == "scissor":
        print("You Won!!")
        user_wins += 1

    elif user_input == "scissor" and computer_pick == "paper":
        print("You Won!!")
        user_wins += 1
        
    elif user_input == "paper" and computer_pick == "rock":
        print("You Won!!")
        user_wins += 1
    else:
        print("You lost!")
        computer_wins += 1

print("You wins ",user_wins, " times.")
print("The computer wins ",computer_wins, " times.")
print("GoodBye!")
        

     