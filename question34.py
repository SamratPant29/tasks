print("Welcome to the Jungle Adventure!")

choice1_data = input("Do you want to go 'left' or 'right'? ").lower()

if choice1_data == "right":
    print("Game Over")
elif choice1_data == "left":
    choice2_data = input("Do you want to \n 'climb a tree' \n  'explore the cave'?\n ").lower()
    if choice2_data == "climb a tree":
        print("Game Over")
    elif choice2_data== "explore the cave":
        choice3_data = input("Choose between \n' bear' \n 'tiger' \n 'snake' \n: ").lower()
        if choice3_data == "bear" or choice3_data == "tiger":
            print("Game Over")
        elif choice3_data == "snake":
            print("You Win")
        else:
            print("Invalid choice. Game Over")
    else:
        print("Invalid choice. Game Over")
else:
    print("Invalid choice. Game Over")