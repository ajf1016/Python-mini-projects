import random

user_wins= 0
computer_wins = 0

options = ["rock","paper","scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q for Quite: ").lower()
    
    if user_input == "q":
        break
    
    if user_input not in options:
        continue
    
    random_number = random.randint(0,2)
    computer_pick = options[random_number]
    
    print("Computer picked " + computer_pick + ".")
    
    if user_input == "rock" and computer_pick == "scissors":
        print("you Won..")
        user_wins += 1
    elif user_input == "paper" and computer_pick == "rock":
        print("you Won..")
        user_wins += 1
    elif user_input == "scissors" and computer_pick == "paper":
        print("you Won..")
        user_wins += 1
    elif user_input ==computer_pick:
        print("its a Tie")
        user_wins += 1
        computer_wins +=1
    else:
        print("You Lost, Computer Won..")
        computer_wins += 1
       
    

print("You won " + str(user_wins) + " Times")
print("Computer won " + str(computer_wins) + " Times")
print("Thank you..!")