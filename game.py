import random

def convert_choice(player_choice): #Convert player's str choice to int.
    if player_choice in ("Rock", "rock"):
        return 1
    elif player_choice in ("Paper", "paper"):
        return 2
    elif player_choice in ("Scissors", "scissors"):
        return 3
    else:
        return 0

def find_winner(choice): #Evaluate who wins the game.
    if choice == 0: 
        return "Oops, incorrect input!"
    comp_choice = random.randint(1,3)
    if comp_choice == choice:
        return "It's a tie!"
    elif comp_choice == 1:
        if choice == 2:
            return "Computer chose rock. You win!"
        elif choice == 3:
            return "Computer chose rock. You lose!"
    elif comp_choice == 2:
        if choice == 1:
            return "Computer chose paper. You lose!"
        elif choice == 3:
            return "Computer chose paper. You win!"
    elif comp_choice == 3:
        if choice == 1:
            return "Computer chose scissors. You win!"
        elif choice == 2:
            return "Computer chose scissors. You lose!"
    

keep_going = "Y"

while keep_going in ("Y", "y"):
    x = input("Choose Rock, Paper, or Scissors: ")

    if type(x) is not str:
        break

    else:
        print(find_winner(convert_choice(x)))

        keep_going = input("Play Again? <Y/N>: ")

print("Thanks for playing!")