import random

user_wins =0
comp_wins =0

options = ["rock", "paper", "scissor"]

while True:

    user_input = input("Type Rock/Paper/Scissor or Q to quit: ").lower()

    if user_input == "q":
        break
    if user_input not in options:
        continue

    random_num = random.randint(0, 2)
    comp_pick = options[random_num]
    print("Computer picked", comp_pick +".")

    if user_input == "rock" and comp_pick == "scissor":
        print("You win!")
        user_wins += 1
        
    elif user_input == "paper" and comp_pick == "rock":
        print("You win!")
        user_wins += 1
        
    elif user_input == "scissor" and comp_pick == "paper":
        print("You win!")
        user_wins += 1
        
    else:
        print("You lost :(")
        comp_wins += 1

print("You won", user_wins,"times.")
print("Computer won", comp_wins,"times.")
print("Goodbye!")